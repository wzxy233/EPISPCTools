# EPISPCTools:Evaluation of personal information security protection capabilities Tools 

# 个人信息安全保护能力评价工具

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

```
pip install django
```

### 数据库操作
更改完models.py后，请进行如下操作。

```
python manage.py makemigrations
python manage.py migrate
```

### 运行
```python manage.py runserver
python manage.py runserver
```

### vue 安装
请阅读vue官方文档 https://cn.vuejs.org/guide/introduction.html 安装Node.js，学习vue的项目页面的搭建方式和与django后端交互方式
```
npm install @vue/cli
```


### vue项目本地运行
```
npm install -g cnpm # 换用淘宝源cnpm
cnpm install
npm run serve
```

### element-plus前端页面搭建
请阅读element-plus官方文档https://element-plus.org/zh-CN/component/overview.html 学习组建使用方法，可以通过https://element-plus.run/ 线上平台进行页面搭建再迁移到项目中

## 进度

- 完成管理系统搭建
- 完成指标体系导入