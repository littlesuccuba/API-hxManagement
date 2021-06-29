from django.db import models
from django_filters.rest_framework import FilterSet
import django_filters
from order.models import OrderInfo

# 过滤器类
class OrderInfoFilter(FilterSet):
    order_id = django_filters.CharFilter(field_name='order_id', lookup_expr='icontains')  # icontains为该字段包含搜索的数据且忽略大小写
    goods_type = django_filters.CharFilter(field_name='goods_type', lookup_expr='icontains')
    user = django_filters.CharFilter(field_name='user', lookup_expr='icontains')
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='state', lookup_expr='icontains')
    class Meta:
        models = OrderInfo
        fields = ['order_id','goods_type','user','phone','state']      # 需要模糊匹配的字段