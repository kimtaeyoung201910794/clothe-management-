
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_view
from clothe import views as clothe_view
from post import views as post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account_view.load),
    path('home/',account_view.home,name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('forgot_passward/', account_view.forgot_password,name='forgot_password'),
    path('register/',account_view.register,name='register'),
    path('search/',clothe_view.search,name='search'),
    path('clothe/add',clothe_view.add,name='add_clothe'),
    path('clothe/view/<str:view_for>',clothe_view.list,name = "clothe_view"),
    path('community/main',post_view.main,name = 'community_main'),
    path('mylooks/',clothe_view.mylooks,name = 'mylooks'),
    path('favorites/',clothe_view.favorite,name = 'favorite'),
    path('weather/',clothe_view.weather,name = 'weather'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/',account_view.setting,name = 'settings'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
