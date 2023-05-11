from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Customer

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # saving the registered user
            user = form.save()
            Customer.objects.create(user=user, name=user.username, email=user.email)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()  # creates an empty form
    return render(request, 'register/signup.html', {'form': form, })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, f"Noto'g'ri kiritildi, Qaytadan urinib ko'ring!")
            return redirect('login')
    else:
        return render(request, 'register/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')