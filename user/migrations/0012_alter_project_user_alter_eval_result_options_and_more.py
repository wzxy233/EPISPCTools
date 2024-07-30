# Generated by Django 5.0.7 on 2024-07-30 02:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0011_alter_user_password_project_eval_result"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
        migrations.AlterModelOptions(
            name="eval_result",
            options={"verbose_name": "评估结果管理", "verbose_name_plural": "评估结果管理"},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"verbose_name": "项目管理", "verbose_name_plural": "项目管理"},
        ),
        migrations.AlterField(
            model_name="eval_result",
            name="eval_result",
            field=models.CharField(
                choices=[
                    ("符合", "符合"),
                    ("部分符合", "部分符合"),
                    ("不符合", "不符合"),
                    ("不适用", "不适用"),
                ],
                default="不适用",
                max_length=5,
                verbose_name="评估结果",
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
