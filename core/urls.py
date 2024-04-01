from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls.static import static
from django.conf import settings


app_name='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.check_form, name='task'),
    path('about/', views.about, name='about') ,
    path('terms/', views.term_of_use, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


