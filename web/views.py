import json

from django.shortcuts import render, HttpResponse, redirect
from web.models import Department, UserInfo
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny

# Create your views here.
def index(request):
    return HttpResponse('欢迎来到学习乐园')

# @csrf_exempt
def depart_list(request):
    if request.method == 'GET':
        return render(request, 'depart_list.html')

    data_list = Department.objects.all()
    data_list = serializers.serialize("json", data_list)
    # data_list = [
    #     {
    #         'id': 1,
    #         'title': 'adfads',
    #     }
    # ]
    count = len(data_list)
    res = {
        'code': 0,
        'msg': '',
        'count': count,
        'data': data_list
    }
    return JsonResponse(res, safe=False)
def depart_list_data(request):
    data_list = Department.objects.all().values()
    count = len(data_list)
    data_list = list(data_list)
    # data_list = serializers.serialize("json", data_list)
    # data_list = [
    #     {
    #         'id': x,
    #         'title': str(x)+'adfads',
    #     }for x in range(10)
    # ]

    res = {
        'code': 0,
        'msg': '',
        'count': count,
        'data': data_list
    }
    return JsonResponse(res, safe=False)

@xframe_options_exempt
def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    msg = {}
    msg['flag'] = 0
    title = request.POST.get('title')
    res = Department.objects.create(title=title)
    if res:
        msg['flag'] = 2
        msg['msg'] = '新增成功'
    else:
        msg['msg'] = '新增失败'
    return HttpResponse(json.dumps(msg))
    # return JsonResponse(msg, safe=False)

# @xframe_options_exempt
def depart_delete(request):
    msg = {}
    msg['flag'] = 0
    get_msg = request.GET
    id = request.GET.get('ID')
    res = Department.objects.filter(id=id).delete()
    if res[0]:
        msg['flag'] = 1
        msg['msg'] = '删除成功'
    else:
        msg['msg'] = '删除失败'
    return JsonResponse(msg, safe=False)

def test(request):
    return render(request, 'test.html')


# modelForm
from django import forms

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'gender', 'department']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'layui-input'}),
        #     'password': forms.TextInput(attrs={'class':'layui-input'}),
        #     'age': forms.TextInput(attrs={'class':'layui-input'}),
        #     'account': forms.TextInput(attrs={'class':'layui-input'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'layui-input'}


def user_list(request):
    if request.method == 'GET':
        return render(request, 'user_list.html')

    # 数据库查询
    # user_list_data = UserInfo.objects.all()
    # for user in user_list_data:
    #     print(user.get_gender_display()) # 性别对应code
    #     print(user.department.title) # 外键名称
    user_list_data = UserInfo.objects.all().values()
    count = len(user_list_data)
    data_list = list(user_list_data)

    res = {
        'code': 0,
        'msg': '',
        'count': count,
        'data': data_list
    }
    return JsonResponse(res, safe=False)

def user_list_data(request):
    user_list_data = UserInfo.objects.all().values()
    count = len(user_list_data)
    data_list = list(user_list_data)

    res = {
        'code': 0,
        'msg': '',
        'count': count,
        'data': data_list
    }
    return JsonResponse(res, safe=False)

@xframe_options_exempt
def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    msg = {}
    msg['flag'] = 0
    title = request.POST.get('title')
    res = UserInfo.objects.create(title=title)
    if res:
        msg['flag'] = 2
        msg['msg'] = '新增成功'
    else:
        msg['msg'] = '新增失败'
    return HttpResponse(json.dumps(msg))