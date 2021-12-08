from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import CustomUsers, Staffs, Course, Student, Subject
import datetime

def adminHome(request):
    return render(request, 'AdminViews/home_content.html')


def addstaff(request):
    return render(request, 'AdminViews/add_Staff.html')

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
    try:    
        user=CustomUsers.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2,)
        user.staffs.address=address
        user.save()
        messages.success(request,"Successfully Added Staff")
        return HttpResponseRedirect(reverse("addstaff"))    
    except:   
        messages.error(request,"Failed to Add Staff")
        return HttpResponseRedirect(reverse("addstaff"))



def addcourse(request):
    return render(request, 'AdminViews/addcourse.html')


def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Course(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("addcourse"))
        except:
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect(reverse("addcourse"))

def addstudent(request):
    courses=Course.objects.all()
    return render(request, 'AdminViews/addnewstudent.html',{"courses":courses})


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        course_id=request.POST.get('course')
        gender=request.POST.get('sex')
    try:   
        user=CustomUsers.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3,)
        user.student.address=address
        course_obj=Course.objects.get(id=course_id)
        user.student.course_id=course_obj
        user.student.session_start=session_start
        user.student.session_end=session_end
        user.student.gender=gender
        user.student.profile_pic=""
        user.save()
        messages.success(request,"Successfully Added Student")
        return HttpResponseRedirect(reverse("addstudent"))    
    except:   
        messages.error(request,"Failed to Add Student")
        return HttpResponseRedirect(reverse("addstudent"))    


def addsubject(request):
    courses=Course.objects.all()
    staffs=CustomUsers.objects.filter(user_type=2)
    return render(request, 'AdminViews/addsubject.html',{'staffs':staffs,'courses':courses})


def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course')
        course=Course.objects.get(id=course_id)
        staff_id=request.POST.get('staff')
        staff=CustomUsers.objects.get(id=staff_id)
    try:
        subject=Subject(subject_name=subject_name,course_id=course,staff_id=staff)
        subject.save()
        messages.success(request,"Successfully Added Subject")
        return HttpResponseRedirect(reverse("addsubject"))    
    except:   
        messages.error(request,"Failed to Add Subject")
        return HttpResponseRedirect(reverse("addsubject"))    


def managestaff(request):
    staffs=Staffs.objects.all()
    return render(request, 'AdminViews/managestaff.html',{'staffs':staffs})

def managestudent(request):
    students=Student.objects.all()
    return render(request, 'AdminViews/managestudent.html',{'students':students})

def managecourse(request):
    courses = Course.objects.all()
    return render(request, 'AdminViews/managecourse.html',{'courses':courses})

def managesubject(request):
    subjects = Subject.objects.all()
    return render(request, 'AdminViews/managesubject.html',{'subjects':subjects})