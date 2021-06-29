from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.ser import UserSer
from users.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import View
from users.sendMessage import SendSms
from django.core.cache import cache
from django.http import HttpResponse
from rest_framework import mixins, status
from rest_framework.response import Response
from users.filters import UserInfoFilter

# Create your views here.

Users = get_user_model()
# 重写jwt认证接口
class CustomBackend(ModelBackend):
    # 手机号或用户名登陆
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 获取用户对象
        user = Users.objects.get(Q(username=username) | Q(phone=username))
        try:
            # 尝试验证密码
            if user.check_password(password):
                return  user
        except Exception as e:
            return None


# 获取短信验证码
class send(View):
    def get(self,request):
        phone = request.GET.get('phone')
        if phone is not None:
            code = SendSms.Send(phone)
            if not cache.get('code') is None:
                return HttpResponse(status=200, content='发送成功')
            else:
                return HttpResponse(status=204, content='发送失败')
        else:
            return HttpResponse(status=204, content='手机号不能为空')



# 用户注册
class UserRegister(mixins.CreateModelMixin, GenericViewSet):
    # 用户注册无需认证与权限
    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSer
    # 重写创建用户方法，先验证短信验证码正确才允许注册，否则返回403错误
    def create(self, request, *args, **kwargs):
        # 验证验证码结果：正确则注册，错误则返回异常
        if request.data.get('code') == cache.get('code'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # 每次使用完验证码后必须销毁该验证码，防止恶意注册
            cache.set('code','', timeout=0)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'code': '403','message': '验证码验证失败'}, status=status.HTTP_403_FORBIDDEN)


# 用户信息查询
class UserViewset(ModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSer
    filterset_class = UserInfoFilter