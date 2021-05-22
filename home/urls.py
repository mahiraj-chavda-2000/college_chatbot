from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path("",views.home ,name ="home"),
     path("",views.index ,name ="index"),
     path("home/",views.home ,name ="home"),
    
     path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
     path('logout/', views.logoutUser, name="logout"),  
     
     path("detail",views.datail_of ,name ="detail"),
     path("colleges",views.colleges ,name ="colleges"),
     path("services",views.services ,name ="services"),
     path('contact', views.contact, name='contact'),
     path('about', views.about, name='about'),
     path('bot', views.bot, name='bot'),
      

     path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),

     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),

     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
]