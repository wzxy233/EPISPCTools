from django.contrib import admin

from .models import *

#后台主页名称
admin.site.site_header = "个人信息影响评估管理系统"
admin.site.site_title = "个人信息影响评估后台管理系统"
admin.site.index_title = "指标体系与用户管理"

#用户管理
class User_Admin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User,User_Admin)

# 评估类管理
class Eval_class_Admin(admin.ModelAdmin):
    list_display = ('eval_class_id', 'eval_class_name')
    list_per_page = 20
    
admin.site.register(Eval_class, Eval_class_Admin)

#评估对象管理
class Eval_item_Admin(admin.ModelAdmin):
    list_display = ('eval_item_id', 'eval_class_name', 'eval_item_name')
    list_filter = ('eval_class_name',)  # 筛选
    list_per_page = 20

admin.site.register(Eval_item,Eval_item_Admin)

class Eval_indicator_Admin(admin.ModelAdmin):
    list_display = ('eval_indicator_id', 'eval_class_name', 'eval_item_name', 'eval_indicator_name', 'weight')
    list_per_page = 20
    list_filter = ('eval_class_name',)  # 筛选

admin.site.register(Eval_indicator, Eval_indicator_Admin)
# Register your models here.
