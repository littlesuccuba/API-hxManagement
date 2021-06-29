from django.db import models

# Create your models here.

# 订单信息表
class OrderInfo(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50)
    goods_type = models.CharField(max_length=30)
    goods_price = models.CharField(max_length=60)
    quantity = models.CharField(max_length=6)
    user = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=40)
