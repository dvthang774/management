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
        return HttpResponse("<h2>Method Not Allowed</h2>")
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
        return HttpResponse("<h2>Method Not Allowed</h2>")
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
        return HttpResponse("<h2>Method Not Allowed</h2>")
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
        student_code=request.POST.get('student_code')
        gender=request.POST.get('sex')
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

    try:   
        user=CustomUsers.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3,)
        user.student.address=address
        user.student.student_code=student_code
        course_obj=Course.objects.get(id=course_id)
        user.student.course_id=course_obj
        user.student.session_start=session_start
        user.student.session_end=session_end
        user.student.gender=gender
        user.student.profile_pic=profile_pic_url
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
        return HttpResponse("<h2>Method Not Allowed</h2>")
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

def editstaff(request, staff_id):
    staff=Staffs.objects.get(admin=staff_id)    
    return render(request, 'AdminViews/editstaff.html',{'staff':staff})


def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        try:    
            user=CustomUsers.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.username=username
            user.email=email
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()  
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/editstaff/"+staff_id)    
        except:   
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/editstaff/"+staff_id)


def editstudent(request, student_id):
    courses = Course.objects.all()
    student=Student.objects.get(admin=student_id)    
    return render(request, 'AdminViews/editstudent.html',{'student':student,'courses':courses})


def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        course_id=request.POST.get('course')
        student_code=request.POST.get('student_code')
        gender=request.POST.get('sex')
        
        if request.FILES.get('profile_pic',False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url=None
        

        user=CustomUsers.objects.get(id=student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email 
        user.student
        user.save()
    try:           
        student=Student.objects.get(admin=student_id)
        student.address=address
        student.session_start_year=session_start
        student.session_end_year=session_end
        student.gender=gender
        student.student_code=student_code
        course=Course.objects.get(id=course_id)
        student.course_id=course
        if profile_pic_url!=None:
            student.profile_pic=profile_pic_url

        student.save()
        messages.success(request,"Successfully Edited Student")
        return HttpResponseRedirect("/editstudent/"+student_id)   
    except: 
        messages.error(request,"Failed to Edit Student")
        return HttpResponseRedirect("/editstudent/"+student_id)


def editcourse(request, course_id):
    course=Course.objects.get(id=course_id)    
    return render(request, 'AdminViews/editcourse.html',{'course':course})
    

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get('course_id')
        course_name=request.POST.get('course')
    try: 
        course=Course.objects.get(id=course_id)   
        course.course_name=course_name
        course.save()

        messages.success(request,"Successfully Edited Course")
        return HttpResponseRedirect("/editcourse/"+course_id)
    except:  
        messages.error(request,"Failed to Edit Course")
        return HttpResponseRedirect("/editcourse/"+course_id)



def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get('subject_id')
        subject_name=request.POST.get('subject_name')
        staff_id=request.POST.get('staff')
        course_id=request.POST.get('course')

        try: 
            subject=Subject.objects.get(id=subject_id)   
            subject.subject_name=subject_name
            staff=CustomUsers.objects.get(id=staff_id)
            course=Course.objects.get(id=course_id)
            subject.staff_id=staff
            subject.course_id=course
            subject.save()

            messages.success(request,"Successfully Edited Subject")
            return HttpResponseRedirect("/editsubject/"+subject_id)
        except:  
            messages.error(request,"Failed to Edit Subject")
            return HttpResponseRedirect("/editsubject/"+subject_id)
    

def editsubject(request, subject_id):
    subject=Subject.objects.get(id=subject_id)
    courses=Course.objects.all()
    staffs=CustomUsers.objects.filter(user_type=2)
    return render(request,'AdminViews/editsubject.html',{'subject':subject, 'courses':courses, 'staffs':staffs})



