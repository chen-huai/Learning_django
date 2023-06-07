

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def chart_list(request):
    return render(request, 'chart_list.html')

def chart_bar(request):
    # 柱状图数据
    legend = ['销量']
    x_list = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    data_list = [
            {
                'name': '销量',
                'type': 'bar',
                'data': [5, 20, 36, 10, 10, 100]
            },
            {
                'name': '销量',
                'type': 'line',
                'data': [5, 20, 36, 16, 10, 100]
            },
        ]

    res = {
        'status': True,
        'data':{
            'legend': legend,
            'x_list': x_list,
            'data_list': data_list
        }
    }
    return JsonResponse(res)