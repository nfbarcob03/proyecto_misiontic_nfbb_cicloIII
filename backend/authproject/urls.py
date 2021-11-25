"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('userInmueble/<int:pk>/', views.UserInmueblesDetailView.as_view()),
    path('users/', views.AllUsers.as_view()),


    path('user2/<int:pk>/', views.UserUpdate.as_view()),
  

    path('tipoInmueble/', views.TipoInmuebleView.as_view()),
    path('tipoInmuebles/', views.AllTipoInmueble.as_view()),
    path('tipoInmueble/<int:pk>/', views.TipoInmuebleView.as_view()),
    path('tipoInmueble/<int:pk>/', views.TipoInmuebleView.as_view()),
    path('tipoInmueble/<int:pk>/', views.TipoInmuebleView.as_view()),

    path('inmueble/', views.InmuebleView.as_view()),
    path('inmuebles/',views.AllInmuebles.as_view()),
    
    path('inmueble/<int:pk>/', views.InmuebleView.as_view()),
    path('inmueble/<int:pk>/', views.InmuebleView.as_view()),
    path('inmueble/<int:pk>/', views.InmuebleView.as_view()),
]