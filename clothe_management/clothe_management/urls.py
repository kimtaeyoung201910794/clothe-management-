
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account_view.home,name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('register/',account_view.register,name='register')
]
