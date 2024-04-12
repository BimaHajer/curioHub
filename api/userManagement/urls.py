from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', view.Inscription.as_view(), name='inscrption'),
    path('login/', view.LoginView.as_view(),name='login'),
    path('logout/',view.LogoutView.as_view(),name="logout"),

]