from django.db import models
from django.contrib.auth.models import AbstractUser
from users.utils import UploadFilesReName
# Create your models here.

# 重写用户信息表
class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True,null=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, upload_to=UploadFilesReName.rename)
