from django.urls import path
from . import views

urlpatterns = [
    path('soils/', views.soil_list, name='soil_list'),
]