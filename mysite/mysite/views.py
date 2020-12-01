from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context, )

def runoob_demo(request):
    views_list = ["骚猪", "二娃", "扎克"]
    views_dict = {"name": "掰子失聪", "age": 18}
    name = 'shAdow'
    num = 1024
    now = datetime.datetime.now()
    null_list = []
    z_name = "二娃锅"
    return render(request, "runoob.html", {"views_list": views_list, "views_dict": views_dict, "name": name, "num": num, "date": now, "null_list": null_list, "z_name": z_name})

def base(request):
    return render(request, 'base.html', None)

def base_extends(request):
    return render(request, 'extends_base.html', None)