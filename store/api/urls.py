from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet

name = "api"

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
