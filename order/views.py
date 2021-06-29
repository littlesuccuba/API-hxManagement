from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from order.models import OrderInfo
from order.ser import OrderSer
from order.filters import OrderInfoFilter
# Create your views here.


class OrderViewset(ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSer
    filterset_class = OrderInfoFilter