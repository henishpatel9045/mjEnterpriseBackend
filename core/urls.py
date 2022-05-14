from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("site", views.SiteInfoViewSet, basename="SiteInfo ViewSet")
router.register("about", views.AboutImageViewSet, basename="About us Images")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("message.urls"))
]
