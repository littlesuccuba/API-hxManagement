from django.db.models import fields
from order.models import OrderInfo
from rest_framework.serializers import ModelSerializer

class OrderSer(ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'