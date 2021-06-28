from rest_framework.serializers import ModelSerializer
from goods.models import GoodsInfo

# 定义序列化器
class GoodsSer(ModelSerializer):
    class Meta:
        model = GoodsInfo
        fields = '__all__'