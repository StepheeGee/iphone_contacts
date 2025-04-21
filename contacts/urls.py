from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_vcf, name='upload_vcf'),
]
