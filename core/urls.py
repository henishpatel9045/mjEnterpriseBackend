from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("site", views.SiteInfoViewSet, basename="SiteInfo ViewSet")
router.register("about", views.AboutImageViewSet, basename="About us Images")
router.register("offer", views.OffersViewSet, basename="Offers")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("message.urls")),
    path("csrf", views.csrf)
]
