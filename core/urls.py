from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.site_info, name="Site-Information"),
    path('about/', views.about_images, name="About Images"),
]
