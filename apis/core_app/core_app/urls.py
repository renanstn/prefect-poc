from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from core.api import viewsets as api_viewsets


router = routers.DefaultRouter()

router.register("ping", api_viewsets.HelloViewSet, basename="ping")
router.register("celery", api_viewsets.CeleryViewSet, basename="celery")
router.register(
    "start_flux", api_viewsets.StartFluxViewSet, basename="start_flux"
)
router.register("run", api_viewsets.RunViewSet, basename="run")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
