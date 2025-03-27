from django.urls import path
from .views import Api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/home", Api)

urlpatterns = router.urls