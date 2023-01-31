from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect(dashboard)

        else:
            messages.error(request, 'Invalid login credentials!')
            return redirect(login)


    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return redirect('home')


def register(request):
    if request.method == "POST":
        # messages.error(request, 'This is an error message')
        # return redirect('register')
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already taken.')
                else:
                    user = User.objects.create_user(first_name = first_name,
                    username=username, password=password, last_name = last_name, email=email)
                    auth.login(request, user)
                    user.save()
                    messages.success(request, 'You are logged in.')
                    return redirect('dashboard')

        else:
            messages.error(request, 'password and confirm password do not match')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')