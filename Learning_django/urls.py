"""
URL configuration for Learning_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from web import views

from web import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('', views.index),
    path('test/', views.test),


    path('depart/list/data/', views.depart_list_data),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),


    path('user/list/', views.user_list),
    path('user/list/data/', views.user_list_data),
    path('user/add/', views.user_add),
    path('user/edit/<int:id>/', views.user_edit),
    path('user/delete/<int:id>/', views.user_delete),


    path('login/', login.login)
]
