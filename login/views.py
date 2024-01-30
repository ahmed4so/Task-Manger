from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Singup
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        user =  authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("Home")

        else:
            message=messages.error(request,"Invalid Username or Password")
            return render(request,"login/login.html",{"message":message})

    else:
        return render(request,"login/login.html")


def signup(request):
    if request.method == "POST":
        # Create user and user profile
        full_name = request.POST.get("full_name")
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        gender = request.POST.get("gender")

        user = User.objects.create_user(username, email, password)
        user_profile = Singup(user=user, gender=gender,fullname=full_name)
        user_profile.save()
        return redirect('login')
    return render(request, 'login/Signup.html')



def logout_view(request):
    logout(request)
    return redirect('login')