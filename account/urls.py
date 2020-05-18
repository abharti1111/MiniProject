from django.urls import path
from .views import PoliceStationView,HomePageView,AboutUsPageView,ContactsPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/',PoliceStationView.as_view(),name='policestation'),
    path('',HomePageView.as_view(),name='home'),
    path('aboutus/',AboutUsPageView.as_view(),name='aboutus'),
    path('contactus/',ContactsPageView.as_view(),name='contactus'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name= 'account/login.html'),name='login'),
]
