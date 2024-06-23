from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,RegionViewSet,ClassViewSet

router = DefaultRouter()
router.register(r'user-message', UserViewSet)
router.register(r'region', RegionViewSet)
router.register(r'class', ClassViewSet)


urlpatterns = [
    path('', include(router.urls)),
]



