from django.db import models
# Create your models here.

# 商品信息表
class GoodsInfo(models.Model):
    g_id = models.AutoField(primary_key=True)
    goods_id = models.CharField(max_length=255,unique=True)
    goods_name = models.CharField(max_length=255)
    goods_type = models.CharField(max_length=60)
    goods_price = models.CharField(max_length=40)
    goods_num = models.CharField(max_length=10)
    goods_state = models.CharField(max_length=50,default='')
    on_shelves = models.BooleanField(default=False)
    is_show = models.BooleanField(default=False)