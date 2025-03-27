from django.urls import path
from .views import ApiViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/list", ApiViewset, basename="home")

urlpatterns = router.urls