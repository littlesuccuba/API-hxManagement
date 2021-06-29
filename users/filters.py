from django_filters.rest_framework import FilterSet
import django_filters
from users.models import User

# 过滤器类
class UserInfoFilter(FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')  # icontains为该字段包含搜索的数据且忽略大小写
    # phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')
    class Meta:
        models = User
        fields = ['username']      # 需要模糊匹配的字段