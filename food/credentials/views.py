from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password1']
        user=auth.authenticate(password = password ,username=username)

        if user is not None:
            auth.login(request,user )
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password= request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect ('register')
            else:
                user= User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save();
                return redirect('login')
                print("user registered")

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render (request,"register.html")
