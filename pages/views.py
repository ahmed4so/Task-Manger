from django.shortcuts import render,redirect
from .models import tasks
from login.models import Singup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    user = request.user
    return render(request,"pages/index.html",{"user":user})
@login_required
def task(request):
    user = request.user


    user_tasks = tasks.objects.filter(User_name=user)

    return render(request, 'pages/tasks.html', {"tasks": user_tasks})
@login_required
def addtask(request):
        if request.method=="POST":
            user = request.user
            title= request.POST.get("name")
            descript=request.POST.get("description")
            duedate=request.POST.get("duedate")
            data =  tasks(Title=title,Description=descript,Date=duedate,User_name=user)
            data.save()
            return redirect('Tasks')
        else:
            return render(request, 'pages/addtask.html')


@login_required
def account(request):
    user = request.user
    try:
        signup_profile = Singup.objects.get(user=user)
        fullname = signup_profile.fullname
        gender = signup_profile.gender
    except Singup.DoesNotExist:
        fullname = None
        gender = None
    return render(request, 'pages/account.html', {
        "username": user.username,
        "fullname":fullname,
        "EMAIL":user.email,
        "gender":gender})