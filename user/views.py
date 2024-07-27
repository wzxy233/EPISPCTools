# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User

# def login(request):
#     if request.method == "POST":
#         # 获取用户通过POST提交过来的数据
#         usm = request.POST.get('usm')
#         pwd = request.POST.get('pwd')

#         if User.objects.filter(username=usm):
#             if User.objects.filter(username=usm)[0].password == pwd:
#                 return HttpResponse('这是一个软件主页！')
#             else:
#                 return HttpResponse('用户名或密码错误！')
#         else:
#             HttpResponse('用户不存在!')

#     return render(request,'user\login.html')


class ApiUser(viewsets.ViewSet):
    # 只有两个参数，默认路由后缀为方法名，可以添加第三个参数url_path='login'指定
    @action(methods=['post'], detail=False)
    def login(self, request):
        # 对象使用.获取，字典使用['key']获取
        password = User.objects.filter(username=request.data['username']).first().password
        result = {
            "code": 200,
            "msg": "登录成功",
            "body": ""
        }
        if password == request.data['password']:
            return Response(result)
        else:
            result['msg'] = "登陆失败"
            result['code'] = -1
            return Response(result)
    
    @action(methods=['post'], detail=False)
    def register(self, request):
        username = request.data['username']
        password = request.data['password']
        User.objects.create(username=username, password=password)
        result = {
            "code": 200,
            "msg": "注册成功",
            "body": ""
        }
        return Response(result)
# Create your views here.
