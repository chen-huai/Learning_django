from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.permissions import BasePermission
from rest_framework.throttling import BaseThrottle
from web import models
import time


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encodings='utf-8'))
    m.update(bytes(ctime, encodings='utf-8'))
    return m.hexdigest()


# 手动用户认证功能
class MyAuthentication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            # 使用postman会提示用户认证失败
            raise exceptions.AuthenticationFailed('用户认证失败')

    def authenticate_header(self, val):
        pass


class RestView(APIView):
    # 用户认证
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def post(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def put(self, request, *args, **kwargs):
        return HttpResponse('获取')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('获取')


class AuthView(APIView):
    # 用于用户登录认证
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('name')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(name=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            token = md5(user)
            request.session()
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)


class Authtication(object):
    # 用于用户认证
    def authenticate(self, request):
        token = request._request.GET.get('token')
        # 后续就是判断session中token与用户是否一致


class DepartView(APIView):
    # 用于部门增删改查
    authentication_classes = [Authtication]

    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        id = request.GET.get('id')
        print(id)
        try:
            obj = models.Department.objects.filter(id=id)
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '无数据'
                return JsonResponse[ret]
            print(obj.values())
            ret['data'] = list(obj.values())
            ret['msg'] = '查询成功'
            print(ret)
            return JsonResponse(ret)
        except Exception as e:
            return JsonResponse(ret)


class Mypermission(BasePermission):
    # 权限管理
    # 在类全局属性中添加该权限管理，permission_classes = [Mypermission]
    def has_permission(self, request, view):
        # 当权限类型为3时，无权访问
        if request.user.user_type == 3:
            return False
        return True


VISIT_RECORD = {}


class VisitThrottle(BaseThrottle):
    # 访问次数
    # return True#return False表示防问频率太高
    def allow_request(self, request, view):
        # 1.获取用户TP
        remote_addr = request.META.get('REMOTE_ADDR')
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime]
            return True
        history = VISIT_RECORD.get(remote_addr)
        while history and history[-1] < ctime:
            history.pop()
        if len(history) < 3:
            history.insert(0, ctime)
            return True
        return False

    def wait(self):

        return 10
