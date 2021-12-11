from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, Password2Form
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        username = request.POST['username']
        email_exist = User.objects.filter(email = email ).exists()
        user_exist = User.objects.filter(username= username).exists()
        if user_exist:
            messages.error(request, 'Username already exist')
            return redirect('account:register')
        elif email_exist:
            messages.error(request, 'Email is already being used')
            return redirect('account:register')
        elif password == confirm_password:
            # user_object = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, password=password)
            user_object = UserForm(request.POST)
            user_object.save()
            messages.success(request, 'You are now registered and can Login now')
            return redirect('account:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('account:register')

    else:
        pwdform = Password2Form()
        context = {'form': pwdform}
        return render(request, 'accounts/register.html',context)


def login(request):

    if request.method == 'POST':

            username =request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login Successfully')
                return redirect('account:dashboard')
            else:
                messages.error(request, "Username and Password doesn't match" )
                return render(request, 'accounts/login.html')
            endif
    else:
        print("login displayed")
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You are now logged out of system')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')