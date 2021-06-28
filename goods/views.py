from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from goods.models import GoodsInfo
from goods.ser import GoodsSer
# Create your views here.

class GoodsViewset(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = GoodsInfo.objects.all()
    serializer_class = GoodsSer
