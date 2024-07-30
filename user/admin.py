from django.contrib import admin
from .models import *
from user.apps import UserConfig
from django.contrib.admin import AdminSite

#后台主页名称
admin.site.site_header = "个人信息影响评估管理系统"
admin.site.site_title = "个人信息影响评估后台管理系统"
admin.site.index_title = "指标体系与用户管理"


class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )

#用户管理
# class User_Admin(admin.ModelAdmin):
#     list_display = ('username', 'password')
#     admin_order = 1

# admin.site.register(User,User_Admin)

# 评估类管理
class Eval_class_Admin(admin.ModelAdmin):
    list_display = ('eval_class_id', 'eval_class_name')
    search_fields = ('eval_class_name',)
    list_per_page = 20
    admin_order = 1
    
admin.site.register(Eval_class, Eval_class_Admin)

#评估对象管理
class Eval_item_Admin(admin.ModelAdmin):
    list_display = ('eval_item_id', 'eval_class_name', 'eval_item_name')
    list_filter = ('eval_class_name',)  # 筛选
    search_fields = ('eval_item_name',)
    list_per_page = 20
    admin_order = 2 

admin.site.register(Eval_item,Eval_item_Admin)

# 评估指标管理
class Eval_indicator_Admin(admin.ModelAdmin):
    list_display = ('eval_indicator_id', 'eval_item_name', 'eval_indicator_name', 'weight')
    search_fields = ('eval_indicator_name',)
    list_per_page = 20
    list_filter = ('eval_item_name',)  # 筛选 
    admin_order = 3 
    
admin.site.register(Eval_indicator, Eval_indicator_Admin)

# 评估结果管理
class Eval_result_Admin(admin.ModelAdmin):
    list_display = ('project_name', 'eval_indicator_name', 'eval_result')
    search_fields = ('project_name',)
    list_per_page = 20
    list_filter = ('project_name',)  # 筛选 
    admin_order = 2 

admin.site.register(Eval_result,Eval_result_Admin)

# 项目管理
class Project_Admin(admin.ModelAdmin):
    admin_order = 1
    
admin.site.register(Project, Project_Admin)


# 显示的app注册
menu_define = [
    {
        'app_label': "user",
        'name': "指标体系管理",
        'app_url': '/admin/indicator_manage/',
        'has_module_perms': True,
        'models':
            [
                "Eval_class",
                "Eval_item",
                "Eval_indicator",
            ]
    },
    {
        'app_label': "user",
        'name': "项目管理",
        'app_url': '/admin/project_manage/',
        'has_module_perms': True,
        'models':
            [
                "Project",
                "Eval_result",
            ]
    }
]


def add_my_menu(app_list_data, define):
    # 应用的models
    app_models = None
    for app in app_list_data:
        if app["app_label"] == UserConfig.name:
            app_models = app["models"]
            app_list_data.remove(app)
    insert_index = 0
    for d in define:
        # 重新设置自定义里的所有models
        models = d["models"]
        model_index = 0
        for j in models:
            # 找到与j对应的model
            model = list(filter(lambda x: x["object_name"] == j, app_models))
            if len(model) > 0:
                models[model_index] = model[0]
                model_index += 1
        app_list_data.insert(insert_index, d)
        insert_index += 1


def index_decorator(func):
    # 重写adminsite里的inner方法
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        app_list = templateresponse.context_data['app_list']
        add_my_menu(app_list, menu_define)
        return templateresponse

    return inner


AdminSite.index = index_decorator(AdminSite.index)
AdminSite.app_index = index_decorator(AdminSite.app_index)
# Register your models here.
