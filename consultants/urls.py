from django.urls import path
from .views import consultants_list

urlpatterns = [
    path('consultants/', consultants_list, name='consultants'),
]