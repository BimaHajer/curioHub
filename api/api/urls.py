from django.contrib import admin
from django.urls import path,include
from userManagement import views
import userManagement
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("userManagement.urls")),
    path('',views.SignupPage,name='signup'),
    # path('login/', views.LoginPage, name='login'),
    # path('home/', views.HomePage, name='home'),
    # path('logout/', views.LogoutPage, name='logout'),
]

