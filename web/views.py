import json

from django.shortcuts import render, HttpResponse, redirect
from web.models import Department, UserInfo
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


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
    # 在编辑和新增中，modelform最好不一样，因为需要校验的内容不一样，如：新增判断电话不一样，编辑时无需判断（或者需排除自身那条数据）


    # 校验方式1
    # name = forms.CharField(
    #     label='名称',validators=['正则表达式']
    # )


    class Meta:
        model = UserInfo
        fields = '__all__'
        # fields = ['name', 'password', 'age', 'account', 'gender', 'department']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'layui-input'}),
        #     'password': forms.TextInput(attrs={'class':'layui-input'}),
        #     'age': forms.TextInput(attrs={'class':'layui-input'}),
        #     'account': forms.TextInput(attrs={'class':'layui-input'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 添加样式
            field.widget.attrs = {'class': 'layui-input', 'placeholder': field.label}
    # # 校验方式2:钩子方法
    # def clean_name(self):
    #     txt_name = self.cleaned_data['name']
    #     # # 判断是否存在
    #     # res = UserInfo.objects.filter(name=txt_name).exists()
    #     # # 编辑时需排除自身数据
    #     # row_id=self.instance.pk
    #     # UserInfo.objects.filter(name=txt_name).exclude(id=1)
    #     if len(txt_name) != 'ceshi':
    #         raise ValidationError('格式错误')
    #     else:
    #         return txt_name


def user_list(request):
    if request.method == 'GET':
        # if request.is_secure():
        #     user_list_data = UserInfo.objects.all().values()
        #     count = len(user_list_data)
        #     data_list = list(user_list_data)
        #
        #     res = {
        #         'code': 0,
        #         'msg': '',
        #         'count': count,
        #         'data': data_list
        #     }
        #     return JsonResponse(res, safe=False)
        return render(request, 'user_list.html')

    # Django可以后台传前端代码，并显示html效果
    #导入mark_safe，并用该库处理数据即可

    # 数据库查询
    # user_list_data = UserInfo.objects.all()
    # for user in user_list_data:
    #     print(user.get_gender_display()) # 性别对应code
    #     print(user.department.title) # 外键名
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
    get_data = request.GET
    # 页码
    page = int(get_data['page'])
    limit = int(get_data['limit'])
    start = (page-1)*limit
    end = page*limit
    # 搜索条件
    search_data = {}
    if ('name' in get_data) and (get_data['name'] != '' or get_data['age'] != '' or get_data['gender'] != ''):
        # search_data['name'] = 'test'
        if get_data['name'] != '':
            search_data['name'] = get_data['name']
        if get_data['age'] != '':
            search_data['age'] = get_data['age']
        if get_data['gender'] != '':
            search_data['gender'] = get_data['gender']
        user_list_data = UserInfo.objects.filter(**search_data).values()
    else:
        user_list_data = UserInfo.objects.all().values()
    count = len(user_list_data)
    # 必须转化为列表才可以显示
    data_list = list(user_list_data)[start:end]

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
    form = UserModelForm(data=request.POST)
    # 校验
    res = form.is_valid()
    if res:
        # 添加界面没有的数据
        # form.instance.create_time = ''
        form.save()
        msg['flag'] = 2
        msg['msg'] = '新增成功'

    else:
        msg['msg'] = '新增失败'
    return HttpResponse(json.dumps(msg))
    # return render(request, 'user_add.html', {'form': form})

@xframe_options_exempt
def user_edit(request, id):
    row_data = UserInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_data)
        return render(request, 'user_edit.html', {'form': form})
    msg = {}
    msg['flag'] = 0
    form = UserModelForm(data=request.POST, instance=row_data)
    # 校验
    res = form.is_valid()
    if res:
        form.save()
        msg['flag'] = 2
        msg['msg'] = '更新成功'

    else:
        msg['msg'] = '更新失败'
    return HttpResponse(json.dumps(msg))

def user_delete(request, id):
    msg = {}
    msg['flag'] = 0
    res = UserInfo.objects.filter(id=id).delete()
    if res[0]:
        msg['flag'] = 1
        msg['msg'] = '删除成功'
    else:
        msg['msg'] = '删除失败'
    return JsonResponse(msg, safe=False)

