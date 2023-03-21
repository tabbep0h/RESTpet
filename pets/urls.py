from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import PetViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register(r'pet', PetViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
