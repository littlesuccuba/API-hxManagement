from django.db import models
from django_filters.rest_framework import FilterSet
import django_filters
from goods.models import GoodsInfo

# 过滤器类
class GoodsInfoFilter(FilterSet):
    goods_name = django_filters.CharFilter(field_name='goods_name', lookup_expr='icontains')  # icontains为该字段包含搜索的数据且忽略大小写
    class Meta:
        models = GoodsInfo
        fields = ['goods_name']      # 需要模糊匹配的字段