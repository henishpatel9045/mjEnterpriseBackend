from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("message", views.ReceivedMessageViewSet,
                basename="ReceivedMessage_Viewset")
router.register("subscribe", views.NewsletterSubscriberViewSet,
                basename="Subscribe Viewset")

urlpatterns = router.urls
