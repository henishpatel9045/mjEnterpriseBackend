from rest_framework.serializers import ModelSerializer
from .models import *


class ReceivedMessageSerializer(ModelSerializer):
    class Meta:
        model = ReceivedMessages
        fields = ["name", "email", "phone_number", "message", "ip_address", "date_created"]
        
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
        
        
class NewsletterSubscriberSerializer(ModelSerializer):
    class Meta:
        model = NewsLetterSubscriber
        fields = "__all__"
        