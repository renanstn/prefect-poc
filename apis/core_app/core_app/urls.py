from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from core.api import viewsets as api_viewsets


router = routers.DefaultRouter()

router.register("ping", api_viewsets.HelloViewSet, basename="ping")
router.register(
    "start_flux", api_viewsets.StartFluxViewSet, basename="start_flux"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
