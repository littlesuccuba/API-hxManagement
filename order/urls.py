from django.urls import path
from order import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('order',views.OrderViewset)

urlpatterns = [


]
urlpatterns += router.urls