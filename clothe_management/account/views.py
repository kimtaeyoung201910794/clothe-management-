from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.conf import settings
from account.forms import UserForm
from account.models import myUser
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import string
import random

def load_img():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.naver.com/')

    html = driver.page_source
    #element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'adaptive')))
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)    
    
 
    

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
    load_img()
    return render(request, 'index.html')

def forgot_password(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email')
        try :
            user = myUser.objects.get(email=email)

            if user is not None:
                new_pw_len = 10 # 새 비밀번호 길이

                pw_candidate = string.ascii_letters + string.digits + string.punctuation 
                
                new_pw = ""
                for i in range(new_pw_len):
                    new_pw += random.choice(pw_candidate)
                
                user.set_password(new_pw)
                user.save()
                template = render_to_string('login/email_template.html',{'name':myUser.get_full_name(user),'password':new_pw})
                method_email = EmailMessage(
                    'Your ID is in the email',
                    template,
                    to = [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'login/email_sent.html',context)
        except:
            messages.info(request, 'There is no username along with the email')
    context = {}
    return render(request, "login/forgot_password.html",context)

def setting(request):
    return render(request, 'register/settings.html')
