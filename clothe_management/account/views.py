from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from account.forms import UserForm
from account.models import myUser

def load(request):
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = new_user.username
            new_user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth_login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    return render(request, "register/register.html", {'form': form})

def login(request):
    return render(request,"login/login.html")

def home(request):
    return render(request, 'index.html')