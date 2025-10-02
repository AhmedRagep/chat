from django.urls import path
from . import views
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import *

urlpatterns = [
	path('',views.index,name='index'),
  path('register',CreateView.as_view(
    template_name="user/register.html",
    form_class=UserForm,
    success_url="/"
  ), name='register'),
  path('login',LoginView.as_view(
    template_name="user/login.html",
    authentication_form = loginclassForm,
    success_url='/'
  ),name='login'),
  path("logout", views.logoutview, name="logout"),
  
	path('detail/<str:pk>',views.detail,name='detail'),
	path('frinds',views.frinds,name='frinds'),
	path('add_frinds/<int:pk>',views.add_frinds,name='add_frinds'),
	path('sendMessage/<str:pk>',views.sendMessage,name='sendMessage'),
	path('receiveMessage/<str:pk>',views.receiveMessage,name='receiveMessage'),
	path('getNotification',views.getNotification,name='getNotification'),
]


