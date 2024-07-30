from django.urls import path
from . import views

app_name = "user"
# urlpatterns = [
#     path("", views.login, name="login"),
    
# ]

from rest_framework import routers
from .views import ApiUser

router = routers.DefaultRouter()
# 第一个参数为url前缀，第二个参数是前缀对应的视图集，第三个参数是视图基本名
router.register('userapi', ApiUser, basename='userapi')

urlpatterns = []

urlpatterns += router.urls