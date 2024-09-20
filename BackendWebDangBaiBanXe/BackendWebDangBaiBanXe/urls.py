"""
URL configuration for WebDangBaiBanXe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from profiles import views as profile_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name='home.html')),
    path('home/xeban/', TemplateView.as_view(template_name='xeban.html')),
    path('home/details',TemplateView.as_view(template_name='details.html')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('profile/', profile_views.EditProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', profile_views.SiteLoginView.as_view(), name='login'),
    path('register/', profile_views.SiteRegisterView.as_view(), name='register'),
]

