from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Studentapi, Marksapi

router = DefaultRouter()
router.register("Studentmodel", Studentapi)
router.register("Marksmodel", Marksapi)


urlpatterns = [
    path('', include(router.urls)),
]