from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from faculty.models import faculty_profile,faculty_assessment,faculty_attendence
from student.models import student_reg ,student_leave

def fac_login(request):
    if request.method =='POST':
        username=request.POST.get('staffAccount')
        password=request.POST.get('staffPassword')
        username=str(username)
        password=str(password)
        u       =faculty_profile.objects.filter(username=username)
        p       =faculty_profile.objects.filter(password=password)
        if u.count()==1 and p.count()==1:
            request.session['fac_user']    = username

            return render(request,'faculty_home.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html ')

def fac_profile(request):
    QuerySet    = faculty_profile.objects.all().filter(username=request.session['fac_user'])
    return render(request,'faculty_profile.html',{'fac_data':QuerySet})

def fac_edit_profile(request):
    QuerySet    = faculty_profile.objects.all().filter(username=request.session['fac_user'])
    return render(request,'faculty_profile_edit.html',{'fac_data':QuerySet})

def fac_edit_save(request):
    name            = request.POST.get('name')
    designation     = request.POST.get('designation')
    join_date       = request.POST.get('join_date')
    qualification   = request.POST.get('qualification')
    gender          = request.POST.get('gender')
    mobile          = request.POST.get('mobile')
    email           = request.POST.get('email')
    batchincharge   = request.POST.get('batchincharge')
    blood_grp       = request.POST.get('blood_grp') 
    dob             = request.POST.get('dob')
    address         = request.POST.get('address')
    password        = request.POST.get('password')

    faculty_profile.objects.filter(username=request.session['fac_user']).update(name=name)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(designation=designation)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(join_date=join_date)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(qualification=qualification)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(gender=gender)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(email=email)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(batchincharge=batchincharge)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(blood_grp=blood_grp)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(dob=dob)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(address=address)
    faculty_profile.objects.filter(username=request.session['fac_user']).update(password=password)
                                    
    QuerySet        = faculty_profile.objects.all().filter(username=request.session['fac_user'])
    return render(request,'faculty_profile.html',{'fac_data':QuerySet})

def fac_stud_leave(request):
    QuerySet        = faculty_profile.objects.all().get(username=request.session['fac_user'])
    var             = QuerySet.batchincharge
    QuerySet1       = student_leave.objects.all().filter(batch=var)
    return render(request,'faculty_stud_leave.html',{'leave':QuerySet1})


def fac_leave_save(request):
    if request.method =='POST':
        name            = request.POST.get('fname')
        student_leave.objects.filter(name=name).update(status='Approved')
        QuerySet        = faculty_profile.objects.all().get(username=request.session['fac_user'])
        var             = QuerySet.batchincharge
        QuerySet1       = student_leave.objects.all().filter(batch=var)
        return render(request,'faculty_stud_leave.html',{'leave':QuerySet1})

def create_asses(request):
    if request.method == 'POST' :
        roll_no            = request.POST.get('roll_no')
        name                = request.POST.get('name')
        batch                = request.POST.get('batch')
        asses1           = request.POST.get('asses1')
        asses2             = request.POST.get('asses2')
        asses3              = request.POST.get('asses3')
        rank             = request.POST.get('rank')
       

        obj                 = faculty_assessment(roll_no=roll_no,name=name,batch=batch,asses1=asses1,asses2=asses2,asses3=asses3,
                                     rank=rank)
        obj.save()
        QuerySet        = faculty_profile.objects.all().get(username=request.session['fac_user'])
        var             = QuerySet.batchincharge
        QuerySet1       = faculty_assessment.objects.all().filter(batch=var)
        return render(request,'faculty_stud_assessment.html',{'stud_data':QuerySet1})

 
def fac_add_attend (request):
    if request.method == 'POST' :
        roll_no            = request.POST.get('roll_no')
        name               = request.POST.get('name')
        batch              = request.POST.get('batch')
        date               = request.POST.get('date')
        fhour              = request.POST.get('fhour')
        shour              = request.POST.get('shour')
        thour              = request.POST.get('thour')
        fohour             = request.POST.get('fohour')
       

        obj                 = faculty_attendence(roll_no=roll_no,name=name,batch=batch,date=date,fhour=fhour,shour=shour,thour=thour,
                                     fohour=fohour)
        obj.save()
        QuerySet        = faculty_profile.objects.all().get(username=request.session['fac_user'])
        var             = QuerySet.batchincharge
        QuerySet1       = faculty_attendence.objects.all().filter(batch=var)
        return render(request,'faculty_stud_attendence.html',{'stud_data':QuerySet1})  


def fac_stud_atten(request):
    QuerySet        = faculty_profile.objects.all().get(username=request.session['fac_user'])
    var             = QuerySet.batchincharge
    QuerySet1       = faculty_attendence.objects.all().filter(batch=var)
    return render(request,'faculty_stud_attendence.html',{'stud_data':QuerySet1})
     

            
        



