from django.db import models

# Create your models here.

class Department(models.Model):
    # 部门
    title = models.CharField(verbose_name='部门名称', max_length=32)
    # delete_time = models.DateTimeField(verbose_name='删除时间')
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    #     员工表
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    # 自动生成department_id字段，
    # 因与department有关联，当部门删除；
    #   1.人员表相应的也删除，级联删除，on_delete=models.CASCADE
    #   2.置空，on_delete=models.SET.NULL,null=True,blank=True
    department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)







