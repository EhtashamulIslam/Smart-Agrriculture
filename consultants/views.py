from django.shortcuts import render

# Create your views here.
from .models import Consultant

def consultants_list(request):
    consultants = Consultant.objects.all()
    return render(request, 'consultants.html', {'consultants': consultants})