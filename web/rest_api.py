from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.views import APIView
from rest_framework import exceptions


# 手动用户认证功能
class MyAuthentication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')

    def authenticate_header(self, val):
        pass


class RestView(APIView):
    # 用户认证
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def post(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def put(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('获取')
