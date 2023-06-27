from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
# 使用中间件需要在setting设置,按顺序执行
class M1(MiddlewareMixin):
    """中间件"""

    def process_request(self, request):
        print('m1进来')

        # 当process_request没有返回值时，可以继续走
        # 如果有返回值
        # return HttpResponse('无权访问')

    def process_response(self, request, response):
        print('m1出去')
        return response


class M2(MiddlewareMixin):
    """中间件2"""

    def process_request(self, request):
        print('m2进来')

    def process_response(self, request, response):
        print('m2出去')
        return response


# 登录验证中间件
class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if request.path_info in ['/login/', '/picture/code/', '/rest/test/', '/api/v1/auth/', '/api/v1/depart/']:
            return
        msg = request.session.get('msg', )
        if msg:
            return
        else:
            return redirect('/login/')

    def process_response(self, request, response):
        return response


class AuthTest(BaseAuthentication):
    # 自定义认证
    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        return None
        raise NotImplementedError(".authenticate() must be overridden.")

class Mypermission(BasePermission):
    # 自定义权限管理
    # 在类全局属性中添加该权限管理，permission_classes = [Mypermission]
    def has_permission(self, request, view):
        # 当权限类型为3时，无权访问
        if request.user.user_type == 3:
            return False
        return True