from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from . import models, serializers

# Create your views here.
class ReceivedMessageViewSet(CreateModelMixin, GenericViewSet):
    queryset = models.ReceivedMessages.objects.all()
    serializer_class = serializers.ReceivedMessageSerializer
    

class NewsletterSubscriberViewSet(CreateModelMixin, GenericViewSet):
    queryset = models.NewsLetterSubscriber.objects.all()
    serializer_class = serializers.NewsletterSubscriberSerializer
    
    