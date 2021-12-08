from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .EmailBackend import EmailBackend
from django.contrib import messages
# Create your views here.

app_name = 'back'
def showPage(request):
    return render(request, "index.html") 

def loginPage(request):
    return render(request, "login.html")


def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed </h2>")
    else:
        user=EmailBackend.authenticate(request, username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request, user)
            if user.user_type=='1':
                return HttpResponseRedirect('/adminhome')
            elif user.user_type=='2':
                return HttpResponse('Staff login'+str(user.first_name))
            else:
                return HttpResponse('Student login'+str(user.first_name))
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect('/')


def GetUserDetail(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/') 