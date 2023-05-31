from django.shortcuts import render, HttpResponse, redirect
from web.models import Department, UserInfo
from django.http import JsonResponse
from web.models import UserInfo
from web.encrypt import md5
from web.picture import get_picture
from io import BytesIO
from django import forms
class loginForm(forms.Form):
    name = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'layui-input'})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'layui-input'})
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'layui-input'})
    )
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

def login(requeset):
    if requeset.method == 'GET':
        form = loginForm()
        return render(requeset, 'login.html', {'form': form})
    form = loginForm(data=requeset.POST)
    if form.is_valid():
        data = form.cleaned_data
        user_input_code = form.cleaned_data.pop('code')
        picture_code = requeset.session.get('picture_code', '')
        print(picture_code)
        if picture_code.upper() != user_input_code.upper():
            form.add_error('code', '验证码错误')
        else:
            user = UserInfo.objects.filter(**form.cleaned_data).first()
            if not user:
                # 添加在password后面
                form.add_error('password', '用户名或密码错误')
                # # 添加在用户名后面
                # form.add_error('name', '用户名或密码错误')
                return render(requeset, 'login.html', {'form': form})
            requeset.session['msg'] = {
                'name': user.name,
                'password': user.password
            }
            requeset.session.set_expiry(7200)
            print(requeset.session['msg']['name'])
            return redirect('/depart/list/')
    return render(requeset, 'login.html', {'form': form})

def logout(request):

    request.session.clear()
    # del request.session['msg']
    return redirect('/login/')

def picture_code(requeset):
    # 生成图片
    img, code = get_picture()
    requeset.session['picture_code'] = code
    # 60s有效
    requeset.session.set_expiry(60)
    # 内存中的文件
    file = BytesIO()
    # 保存内存中
    img.save(file, 'png')
    return HttpResponse(file.getvalue())