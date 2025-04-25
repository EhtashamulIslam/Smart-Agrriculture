from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views import View
from django.urls import path
import json
from .utils.ai_chat import ask_agri_expert, chatbot

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ChatbotView(View):
    
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'chatbot_ai/farmer.html')

    @method_decorator(login_required)
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
        
        # Parse the JSON data from the request body
        print(request.body)
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        user_id = data.get('user_id', 'default_user')
        user_messages: list[dict] = data.get('messages', [])
        if user_messages:
            response_message = chatbot(user_messages, user_id)
        else:
            user_message = data.get('message')
            response_message = ask_agri_expert(user_message, user_id)
        return JsonResponse({'reply': response_message})


@login_required
def WeatherView(request):
    return render(request, 'chatbot_ai/weather.html')