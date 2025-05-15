from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('success/', views.donation_success, name='donation_success'),
    path('cancel/', views.donation_cancel, name='donation_cancel'),
]