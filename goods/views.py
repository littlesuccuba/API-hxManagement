from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from goods.models import GoodsInfo
from goods.ser import GoodsSer
from goods.filters import GoodsInfoFilter
# Create your views here.

class GoodsViewset(ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = GoodsInfo.objects.all()
    serializer_class = GoodsSer
    filterset_class = GoodsInfoFilter
