from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def login(request):
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        usm = request.POST.get('usm')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=usm):
            if User.objects.filter(username=usm)[0].password == pwd:
                return HttpResponse('这是一个软件主页！')
            else:
                return HttpResponse('用户名或密码错误！')
        else:
            HttpResponse('用户不存在!')

    return render(request,'user\login.html')

# Create your views here.
