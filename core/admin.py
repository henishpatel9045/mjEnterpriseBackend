from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(SiteInfo)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'businessName', 'last_updated']


@admin.register(AboutImage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'subtitle', 'date_created']


@admin.register(Offers)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', "date_created", "last_updated", "is_listed"]
    list_editable = ['is_listed']
    list_per_page = 10

    search_fields = ["title"]
