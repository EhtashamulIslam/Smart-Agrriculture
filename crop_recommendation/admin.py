from django.contrib import admin
from .models import SoilType, RecommendedCrop

admin.site.register(SoilType)
admin.site.register(RecommendedCrop)