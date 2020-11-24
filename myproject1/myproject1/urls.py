"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home, name='home'),
    path('',views.create, name='create'),
    #path('update/',views.update,name='update'),
    path('update_view/<id>/',views.update_view,name='update_view'),
    #path('update_save/',views.retrive,name='retrive'),
    path('update_view_save/<id>/',views.update_view_save,name='update_view_save'),
    path('delete/<id>/',views.delete,name='delete')
]
