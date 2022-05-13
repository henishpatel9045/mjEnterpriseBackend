from django.db import models
from ckeditor import fields

# Create your models here.


class ReceivedMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    ip_address = models.CharField(max_length=150)    
    response = fields.RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id) + self.name
    
    class Meta:
        ordering = ["response"]
    
    
class NewsLetterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    

class SendMail(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = fields.RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + self.subject 
    
    
    