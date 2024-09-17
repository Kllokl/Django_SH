from django.db import models

# Create your models here.


class Departent(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题',max_length=32) # 创建表

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账号余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    # 级联删除
    depart = models.ForeignKey(to='Departent',to_field='id',on_delete=models.CASCADE)
    # 置空
    # depart2 = models.ForeignKey(to='tables+name',to_field='table_id',null=True,blank=True,on_delete=models.SET_NULL)

    gener_choices = (
        ('男',1),
        ('女',2),
    )

    gender = models.SmallIntegerField(verbose_name='性别',choices=gener_choices)


class user_info(models.Model):
    """练手"""

    user = models.CharField(verbose_name='账号',max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

