# EPISPCTools:Evaluation of personal information security protection capabilities Tools 个人信息安全保护能力评价工具

一个用于等保测评领域个人信息安全保护能力评价的web应用工具，基于django框架开发。

## 功能模块 
- 用户登录认证
- 用户上传测评结果
- 评估结果计算与等级评定
- 管理员给普通用户授权
- 管理员管理指标体系

## 开发者模式
请阅读django官方文档https://docs.djangoproject.com/zh-hans/5.0/intro/install/。
快速安装指南->编写你的第一个django应用1-5部分，为你的计算机安装django，并通过/polls目录下的示例应用与/user目录真实应用进行对比理解user应用的运行逻辑。

### django 安装
'''
pip install django
'''

### 数据库操作
更改完models.py后，请进行如下操作。
'''
python manage.py makemigrations
python manage.py migrate
'''

### 运行
'''
python manage.py runserver
'''