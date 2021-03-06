from django.urls import path
from . import views, adminviews
  
  
urlpatterns = [
    path('index/', views.showPage, name='index'),
    path('', views.loginPage, name='login'),
    path('doLogin/',views.doLogin),
    path('get_user_detail/', views.GetUserDetail),
    path('logout/', views.Logout),
    path('adminhome/', adminviews.adminHome),
   
    path('addstaff/',adminviews.addstaff, name='addstaff'),    
    path('add_staff_save',adminviews.add_staff_save,name="add_staff_save"),
   
    path('addcourse/',adminviews.addcourse, name='addcourse'),
    path('add_course_save',adminviews.add_course_save,name="add_course_save"),
   
    path('addstudent/',adminviews.addstudent, name='addstudent'),
    path('add_student_save',adminviews.add_student_save,name="add_student_save"),
   
    path('addsubject/',adminviews.addsubject, name='addsubject'),
    path('add_subject_save',adminviews.add_subject_save,name="add_subject_save"),
   
    path('managestaff',adminviews.managestaff,name="managestaff"),
    path('managestudent',adminviews.managestudent,name="managestudent"),
    path('managecourse/',adminviews.managecourse,name="managecourse"),
    path('managesubject/',adminviews.managesubject,name="managesubject"),
  
    path('editstaff/<str:staff_id>',adminviews.editstaff,name="editstaff"),
    path('edit_staff_save',adminviews.edit_staff_save,name="edit_staff_save"),
  
    path('editstudent/<str:student_id>/',adminviews.editstudent,name="editstudent"),
    path('edit_student_save',adminviews.edit_student_save,name="edit_student_save"),

    path('editsubject/<str:subject_id>',adminviews.editsubject,name="editsubject"),
    path('edit_subject_save',adminviews.edit_subject_save,name="edit_subject_save"),
    
    path('editcourse/<str:course_id>/',adminviews.editcourse,name="editcourse"),
    path('edit_course_save',adminviews.edit_course_save,name="edit_course_save"),

]