from django.db import models
from ckeditor import fields

# Create your models here.

class SiteInfo(models.Model):
    businessName = models.CharField(max_length=100, default="Mj Enterprise")
    logo = models.ImageField(upload_to="site/")
    aboutUs = fields.RichTextField()
    whatsapp = models.URLField()
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    gmail = models.EmailField()
    phone_number = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=100)
    gst_in_no = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if SiteInfo.objects.count() == 1:
            SiteInfo.objects.all().delete()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.businessName

    class Meta:
        ordering = ['-last_updated']
        verbose_name_plural = "Site Info"
        

class AboutImage(models.Model):
    image = models.ImageField(upload_to="about/")
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if self.subtitle:
            return self.subtitle
        return super().__str__()
    
    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = "About Image"
    

class Offers(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="offers")
    description = fields.RichTextField()
    link = models.URLField(null=True, blank=True)
    is_listed = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['last_updated', 'date_created']
        verbose_name_plural = 'Offers'
