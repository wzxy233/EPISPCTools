from django.db import models
# from django.utils.translation import gettext_lazy as _

class User(models.Model):
    username = models.CharField(max_length=20, primary_key= True, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username

class Eval_class(models.Model):
    eval_class_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_class_name = models.CharField(max_length=20, primary_key=True, verbose_name='评估类名')

    class Meta:
        verbose_name = "评估类管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_class_name

class Eval_item(models.Model):
    eval_item_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_item_name = models.CharField(max_length=20, primary_key=True, verbose_name='评估项名')
    eval_class_name = models.ForeignKey(Eval_class, on_delete=models.CASCADE, verbose_name='评估类')

    class Meta:
        verbose_name = "评估项管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_item_name

class Eval_indicator(models.Model):
    eval_indicator_id = models.PositiveIntegerField(verbose_name='序号', unique=True)
    eval_class_name = models.ForeignKey(Eval_class, on_delete=models.CASCADE, verbose_name='评估类名')
    eval_item_name = models.ForeignKey(Eval_item, on_delete=models.CASCADE, verbose_name='评估项名')
    eval_indicator_name = models.TextField(primary_key= True, max_length=200, unique=True, verbose_name='评估指标名')
    weight =  models.PositiveIntegerField(verbose_name='权重值')
    
    class Meta:
        verbose_name = "评估指标管理"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.eval_indicator_name

# Create your models here.
