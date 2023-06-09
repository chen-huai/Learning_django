from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import pandas as pd
from django import forms
import os



def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')
    print(request.POST)
    print(request.FILES)
    file_obj = request.FILES.get('file')
    # 直接读取数据
    upload_file = pd.read_csv(file_obj)
    # print(upload_file)
    # # file_obj.name文件名
    # f = open(file_obj.name, mode='wb')
    # for chunk in file_obj.chunks():
    #     f.write(chunk)
    # f.close()
    return HttpResponse('test')


class UpForm(forms.Form):
    name = forms.CharField(label='姓名')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField(label='照片')

def upload_form(request):
    if request.method == 'GET':
        form = UpForm()
        print('dd')
        return render(request, 'upload_form.html', {'form': form})

    form = UpForm(request.POST, request.FILES)
    # form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        img = form.cleaned_data.get('img')
        # 上传图片是上传文件路径,需要将路径由static开始
        file_path = os.path.join('web.static.img', 'static', 'img', img.name)
        f = open(file_path, mode='wb')
        for chunk in img.chunks():
            f.write(chunk)
            f.close()
        return HttpResponse('TEST')
    return render(request, 'upload_form.html', {'form': form})