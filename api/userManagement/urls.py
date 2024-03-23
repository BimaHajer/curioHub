from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.LoginPage, name='login'),
   path('home/', views.HomePage, name='home'),
   path('logout/', views.LogoutPage, name='logout'),
   path('user/profile/',views.ProfilePage,name='userprofile'),
   path('confrimeraccount',views.ConfirmerPage,name='confirmer'),
   path('activateaccount',views.ActivatePage,name='activate'),

]