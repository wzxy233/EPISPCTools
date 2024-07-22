from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20,primary_key=True, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="用户名")

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username

class Eval_class(models.Model):
    eval_class_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_class_name = models.CharField(max_length=20, primary_key=True, verbose_name='评估类')

    class Meta:
        verbose_name = "评估类管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_class_name

class Eval_item(models.Model):
    eval_item_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_item_name = models.CharField(max_length=20, primary_key=True, verbose_name='评估项')
    eval_class_name = models.ForeignKey(Eval_class, on_delete=models.CASCADE, verbose_name='评估类')

    class Meta:
        verbose_name = "评估项管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_item_name

class Eval_indicator(models.Model):
    eval_indicator_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_item_name = models.ForeignKey(Eval_item, on_delete=models.CASCADE, verbose_name='评估项')
    eval_indicator_name = models.TextField(primary_key= True, max_length=200, unique=True, verbose_name='评估指标')
    weight =  models.PositiveIntegerField(verbose_name='权重值')
    
    class Meta:
        verbose_name = "评估指标管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_indicator_name


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name = '用户')
    project_name = models.CharField(max_length=50, primary_key= True, verbose_name = "项目名")

    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.project_name


class Eval_result(models.Model):
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE, verbose_name= '项目名')
    eval_indicator_name = models.ForeignKey(Eval_indicator, on_delete = models.CASCADE, verbose_name= '评估项')
    FIT = '符合'
    PART_FIT = '部分符合'
    UNFIT = '不符合'
    UNRELATED = '不适用'
    EVAL_RESULT_CHOICES = (
        (FIT, '符合'),
        (PART_FIT, '部分符合'),
        (UNFIT, '不符合'),
        (UNRELATED, '不适用'),
    )
    eval_result = models.CharField(
        max_length=5,
        choices=EVAL_RESULT_CHOICES,
        default=UNRELATED,
        verbose_name= '评估结果'
    )

    class Meta:
        verbose_name = "评估结果管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.project_name
# Create your models here.
