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
from django.urls import path,re_path
from django.views.static import serve
from Learning_django import settings

from web import views, login, chart, upload, rest_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('', views.index),
    path('test/', views.test),

    #
    re_path(r'media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),

    # 部门
    path('depart/list/data/', views.depart_list_data),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),

    # 用户
    path('user/list/', views.user_list),
    path('user/list/data/', views.user_list_data),
    path('user/add/', views.user_add),
    path('user/edit/<int:id>/', views.user_edit),
    path('user/delete/<int:id>/', views.user_delete),

    # 登录
    path('login/', login.login),
    path('logout/', login.logout),
    path('picture/code/', login.picture_code),

    # 图表
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),

    #  rest framework
    path('rest/test/', rest_api.RestView.as_view()),
    path('api/v1/auth/', rest_api.AuthView.as_view()),
    path('api/v1/depart/', rest_api.DepartView.as_view()),
]
