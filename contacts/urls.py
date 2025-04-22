from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_vcf, name='upload_vcf'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('contact/', views.contact_view, name='contact'),
]

