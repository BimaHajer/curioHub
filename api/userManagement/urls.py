# from django.contrib import admin
# from django.urls import path
# from userManagement.views import InscriptionAPIView
# from . import views

# urlpatterns = [
#    path('login/', views.LoginPage, name='login'),
#    path('home/', views.HomePage, name='home'),
#    path('logout/', views.LogoutPage, name='logout'),
#    path('inscrit/', InscriptionAPIView.as_view(), name='inscription_api'),
#    # path('user/profile/',views.ProfilePage,name='userprofile'),
#    # path('confrimeraccount',views.ConfirmerPage,name='confirmer'),
#    # path('activateaccount',views.ActivatePage,name='activate'),

# ]
from django.urls import path,include
from userManagement import views  as view
urlpatterns = [
    path('register/', view.Inscription.as_view(), name='inscrption'),
    path('login/', view.LoginView.as_view(),name='login'),
    path('logout/',view.LogoutView.as_view(),name="logout"),
    # path('listUser/', view.ListUsers.as_view()),
]