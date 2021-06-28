from django.urls import path
from users import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register('user', views.UserViewset)
router.register('register', views.UserRegister)

urlpatterns = [
    # jwt默认登陆接口
    path('login/', obtain_jwt_token),
    # 短信验证码接口
    path('getcode/', views.send.as_view()),
]
urlpatterns += router.urls