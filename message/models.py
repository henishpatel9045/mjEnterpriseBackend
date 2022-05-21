from django.db import models
from ckeditor import fields
from django.forms import CharField
from .utils import send_single_mail
from django.db.transaction import atomic

# Create your models here.


class ReceivedMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    ip_address = models.CharField(max_length=150, null=True, blank=True)
    response = fields.RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id) + self.name
    
    class Meta:
        ordering = ["response"]
    
    
class NewsLetterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        with atomic():
            # send_single_mail(["ompatel9045@gmail.com"], "New Subscriber added.", "New subscriber added to newsletter subscriber list.")
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    

class SendMail(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = fields.RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        with atomic():
            recepient_list = [
                i.email for i in NewsLetterSubscriber.objects.all()]
            send_single_mail(recepient_list, self.subject, self.body)
            return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + self.subject 
    
    
    