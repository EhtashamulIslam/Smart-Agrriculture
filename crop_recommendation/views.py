from django.shortcuts import render
from .models import SoilType

def soil_list(request):
    soils = SoilType.objects.all()
    return render(request, 'soil/soil_list.html', {'soils': soils})