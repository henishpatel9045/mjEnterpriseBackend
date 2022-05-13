from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ReceivedMessages)
class ReceivedMessagesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date_created", "response_sent"]
    # readonly_fields = ["name", "email", "phone_number", "message", "ip_address"]
    
    def response_sent(self, msg):
        if len(msg.response) > 0:
            return "Yes"
        return "No"
    

@admin.register(NewsLetterSubscriber)
class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    list_display = ["email", "date_created", "mail_send"]
    # readonly_fields = ['email']
    
    def mail_send(self, sub):
        number = SendMail.objects.filter(date_created__gte=sub.date_created).count()
        return number
        

@admin.register(SendMail)
class SendMailAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'date_created']
        