from django.urls import path
from goods import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('good', views.GoodsViewset)

urlpatterns = [

]
urlpatterns += router.urls