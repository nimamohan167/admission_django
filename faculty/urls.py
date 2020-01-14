from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
            #redirecting to various pages  fac_stud_leav-reject

    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('faculty-login-page/',TemplateView.as_view(template_name='login.html'),name='faculty_login_page'),
    path('faculty-leave-frwrd/',TemplateView.as_view(template_name='faculty_leave_forwrd.html'),name='fac_stud_leav-forwrd'),
    path('faculty-leave-reje/',TemplateView.as_view(template_name='faculty_stud_leav_rejected.html'),name='fac_stud_leav_reject'),
    path('faculty-stud-assessment/',TemplateView.as_view(template_name='faculty_stud_assessment.html'),name='student_assessmnt'),
    path('faculty-home/',TemplateView.as_view(template_name='faculty_home.html'),name='faculty_home'),
    path('faculty-home/',TemplateView.as_view(template_name='faculty_home.html'),name='faculty_home'),
    path('student-login/',TemplateView.as_view(template_name='student_login.html'),name='student_home'),
    
   
     #view functions    

    path('faculty/',views.fac_login,name='faculty_login'),
    path('faculty-profile/',views.fac_profile,name='faculty_profile'),
    path('faculty-profile-edit/',views.fac_edit_profile,name='faculty_edit_profile'),
    path('faculty-save-profile/',views.fac_edit_save,name='faculty_edit_save'),
    path('logout/',views.logout_view,name='logout'),
    path('fac-stud-leave/',views.fac_stud_leave,name='student_leave'),
    path('faculty-leave-save/',views.fac_leave_save,name='faculty_leave_save'),
    path('create-assesmnt/',views.create_asses,name='create_assessmnt'),
    path('fac-add-attensdence/',views.fac_add_attend,name='faculty_add_attendence'),
    path('fac-styudentr_attend/',views.fac_stud_atten,name='fac_student_attendence'),
]