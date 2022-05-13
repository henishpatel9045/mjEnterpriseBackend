from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(SiteInfo)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'businessName', 'last_updated']
    

@admin.register(AboutImage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'subtitle', 'date_created']
