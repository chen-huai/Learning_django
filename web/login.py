from django.shortcuts import render, HttpResponse, redirect
from web.models import Department, UserInfo
from django.http import JsonResponse
from web.models import UserInfo
from web.encrypt import md5

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
        user = UserInfo.objects.filter(**data).first()
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
        print(requeset.session['msg']['name'])
        return redirect('/depart/list/')
    return render(requeset, 'login.html', {'form': form})

def logout(request):

    request.session.clear()
    # del request.session['msg']
    return redirect('/login/')