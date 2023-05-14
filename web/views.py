from django.shortcuts import render, HttpResponse
from web.models import Department, UserInfo
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
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
    print(res)
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

def test(request):
    return render(request, 'test.html')