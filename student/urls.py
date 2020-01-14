from django.urls import path
from . import views
from django.views.generic import TemplateView  

urlpatterns=[
            path('student-login-page/',TemplateView.as_view(template_name='student_login.html'),name='student_login_page'),
            
            path('student-home/',TemplateView.as_view(template_name='student_home.html'),name='student_home_page'),
            

          
            path('student/',views.stud_login,name='student_login'),
            path('student-profile/',views.stud_profil,name='stud_profile'),
            path('student-profile-edit/',views.stud_profile_edit,name='stud_edit_profile'),
            path('student-profile-save/',views.stud_prof_edit_save,name='stud_prof_edit_save'),
            path('studen-leav-mangmnt/',views.stud_leave_mngmnt,name='stud_leave_mangmnt'),
            path('studen-leave-apply/',views.stud_leave_apply,name='stud_apply_leave'),
            path('student-logout/',views.st_logout_view,name='st_logout'),
            path('studen-applied-leave/',views.st_appliedleave_view,name='stud_applied_leav'),
            path('student-assesment/',views.st_assessment,name='student_assesmnt'),
            path('stud-attendence/',views.stud_attend,name='student_attendence'),


]