from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('AdminLogin/', views.AdminLogin, name='AdminLogin'),
    path('AdminRegistration/', views.AdminRegistration, name='AdminRegistration'),
    path('DocLogin/', views.DocLogin, name='DocLogin'),
    path('DocRegistration/', views.DocRegistration, name='DocRegistration'),
    path('PatientLogin/', views.PatientLogin, name='PatientLogin'),
    path('PatientRegistration/', views.PatientRegistration, name='PatientRegistration'),
    path('AdminDashboard/', views.AdminDashboard, name='AdminDashboard'),
    path('DoctorDashboard/', views.DoctorDashboard, name='DoctorDashboard'),
    path('PatientDashboard/', views.PatientDashboard, name='PatientDashboard'),

]