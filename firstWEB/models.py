from django.db import models

# Create your models here.

class cal(models.Model):
    value_a = models.CharField(max_length=10) # 字符串
    value_b = models.FloatField(max_length=10) # 浮点数
    result = models.CharField(max_length=10)