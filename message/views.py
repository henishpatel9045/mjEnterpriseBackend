from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from . import models, serializers
from .utils import send_single_mail

# Create your views here.
class ReceivedMessageViewSet(CreateModelMixin, GenericViewSet):
    queryset = models.ReceivedMessages.objects.all()
    serializer_class = serializers.ReceivedMessageSerializer
    

class NewsletterSubscriberViewSet(CreateModelMixin, GenericViewSet):
    queryset = models.NewsLetterSubscriber.objects.all()
    serializer_class = serializers.NewsletterSubscriberSerializer
    
    