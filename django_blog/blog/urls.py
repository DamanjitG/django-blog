from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-homepage'),
    path('about/', views.about, name='blog-about'),                    
]