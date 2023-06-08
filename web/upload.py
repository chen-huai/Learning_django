from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import pandas as pd

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
