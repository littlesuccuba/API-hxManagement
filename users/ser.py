from os import write
from users.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.core.cache import cache

class UserSer(ModelSerializer):
    is_active = serializers.BooleanField(default=True, required=False,help_text='用户是否可登陆', label='是否允许登陆')
    def create(self, validated_data):
        # 将redis缓存中的手机号写入用户信息表
        if validated_data.get('phone') is None:
            validated_data['phone'] = cache.get('phone')
        # # 如果有is_staff属性则为管理员用户，否则为普通用户
        # if validated_data['is_staff']:
        #     # 分配至管理员用户组
        #     validated_data['groups'] = [2]
        # else:
        #     # 分配至普通用户组
        #     validated_data['groups'] = [1]
        # 注册时密码加密方法重写
        user = super(UserSer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # 创建用户成功后销毁redis缓存
        cache.set('phone', '', timeout=0)
        return user
    # 修改密码时密码加密重写
    def update(self, instance, validated_data):
        password = validated_data.get('password')
        userinfo = User.objects.get(id=instance.id)
        user = super(UserSer, self).update(instance = instance, validated_data = validated_data)
        
        if validated_data.get('password') is not None:
            # 判断密码是否与上次的密码相同
            if userinfo.password == password:
                print('密码一致')
            else:
                print('密码不一致')
                user.set_password(password)
                user.save()
                return user
                
        # user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'username': {
                'help_text': '用户名'
            },
            'password': {
                'help_text': '密码',
                'label': '密码',
                # 'write_only': True
            },
            'last_login': {
                'help_text': '最后登录时间（不需要用户提供）'
            },
            'is_superuser': {
                'help_text': '是否为超级管理员',
                'write_only': True
            },
            'email': {
                'help_text': '邮箱（可选）'
            },
            'date_joined': {
                'help_text': '用户注册时间'
            },
            'phone': {
                'label': '手机号',
                'help_text': '手机号码（必须）'
            },
            'is_staff': {
                'write_only': True
            },
            'user_permissions': {
                'label': '用户权限',
                'help_text': '用户所拥有的权限（默认为空）',
                'write_only': True
            },
            'user_permissions': {
                'label': '用户组',
                'help_text': '用户所在用户组，该组拥有一定权限（默认普通用户）',
                'write_only': True
            },
            'avatar': {
                'label': '头像地址',
                'help_text': '用户头像地址(可选)'
            },
            'first_name': {
                'write_only': True
            },
            'last_name': {
                'write_only': True
            }
        }