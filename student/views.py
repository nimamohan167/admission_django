from django.shortcuts import render
from student.models import student_leave,student_reg
from faculty.models import faculty_assessment ,faculty_attendence
from django.contrib.auth import logout
def stud_login(request):
    if request.method =='POST':
        username=request.POST.get('studAccount')
        password=request.POST.get('studPassword')
        username=str(username)
        password=str(password)
        u       = student_reg.objects.filter(username=username)
        p       = student_reg.objects.filter(password=password)
        if u.count()==1 and p.count()==1:
            request.session['stud_user']    = username
            return render(request,'student_home.html')

def st_logout_view(request):
    logout(request)
    return render(request,'student_login.html ')

def stud_profil(request):
    QuerySet    = student_reg.objects.all().filter(username=request.session['stud_user'])
    return render(request,'student_profile.html',{'stud_data':QuerySet})

def stud_profile_edit(request):
    QuerySet    = student_reg.objects.all().filter(username=request.session['stud_user'])
    return render(request,'student_edit_profile.html',{'stud_data':QuerySet})


def stud_prof_edit_save(request):
    admission_no            = request.POST.get('admission_no')
    name                    = request.POST.get('name')
    roll_no                 = request.POST.get('roll_no')
    qualification           = request.POST.get('qualification')
    email                   = request.POST.get('email')
    gender                  = request.POST.get('gender')
    course                  = request.POST.get('course')
    batch                   = request.POST.get('batch')
    dob                     = request.POST.get('dob')
    blood_grp               = request.POST.get('blood_grp') 
    mobile                  = request.POST.get('mobile')
    address                 = request.POST.get('address')
    religion                = request.POST.get('religion')
    category                = request.POST.get('category')

    student_reg.objects.filter(username=request.session['stud_user']).update(admission_no=admission_no)
    student_reg.objects.filter(username=request.session['stud_user']).update(name=name)
    student_reg.objects.filter(username=request.session['stud_user']).update(roll_no=roll_no)
    student_reg.objects.filter(username=request.session['stud_user']).update(qualification=qualification)
    student_reg.objects.filter(username=request.session['stud_user']).update(email=email)
    student_reg.objects.filter(username=request.session['stud_user']).update(gender=gender)
    student_reg.objects.filter(username=request.session['stud_user']).update(course=course)
    student_reg.objects.filter(username=request.session['stud_user']).update(batch=batch)
    student_reg.objects.filter(username=request.session['stud_user']).update(dob=dob)
    student_reg.objects.filter(username=request.session['stud_user']).update(blood_grp=blood_grp)
    student_reg.objects.filter(username=request.session['stud_user']).update(mobile=mobile)
    student_reg.objects.filter(username=request.session['stud_user']).update(address=address)
    student_reg.objects.filter(username=request.session['stud_user']).update(religion=religion)
    student_reg.objects.filter(username=request.session['stud_user']).update(category=category)
                                    
    QuerySet        = student_reg.objects.all().filter(username=request.session['stud_user'])
    return render(request,'student_profile.html',{'stud_data':QuerySet})

def stud_leave_mngmnt(request):
    QuerySet    = student_reg.objects.all().filter(username=request.session['stud_user'])
    return render(request,'student_leave_management.html',{'stud_data':QuerySet})

def stud_leave_apply(request):
    if request.method == 'POST' :
        leave_id            = request.POST.get('leave_id')
        name                = request.POST.get('name')
        batch                = request.POST.get('batch')
        from_date           = request.POST.get('from_date')
        to_date             = request.POST.get('to_date')
        reason              = request.POST.get('reason')
        describ             = request.POST.get('describ')
       

        obj                 = student_leave(leave_id=leave_id,name=name,batch=batch,from_date=from_date,to_date=to_date,reason=reason,
                                     describ=describ)
        obj.save()
        QuerySet    = student_leave.objects.all().filter(name=request.session['stud_user'])
        return render(request,'student_applied_leave.html',{'stud_data':QuerySet})

def st_appliedleave_view(request):
    QuerySet    = student_leave.objects.all().filter(name=request.session['stud_user'])
    return render(request,'student_applied_leave.html',{'stud_data':QuerySet})

def st_assessment(request):
    QuerySet    = faculty_assessment.objects.all().filter(name=request.session['stud_user'])
    return render(request,'student_assessment.html',{'stud_data':QuerySet})


def stud_attend(request):
    QuerySet    = faculty_attendence.objects.all().filter(name=request.session['stud_user'])
    return render(request,'student_assessment.html',{'stud_data':QuerySet})
