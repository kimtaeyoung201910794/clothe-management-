
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_view
from clothe import views as clothe_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account_view.load),
    path('home/',account_view.home,name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('register/',account_view.register,name='register'),
    path('search/',clothe_view.search,name='search'),
    path('clothe/add',clothe_view.add,name='add_clothe'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
