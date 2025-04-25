from django.urls import path

from . import views

app_name = 'ai_chatbot'

urlpatterns = [
    path("farmer", views.ChatbotView.as_view() , name='farmer'),
    path("weather", views.WeatherView, name='weather'),
]
