from django.db import models

# Create your models here.
class SoilType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class RecommendedCrop(models.Model):
    soil_type = models.ForeignKey(SoilType, on_delete=models.CASCADE, related_name='crops')
    crop_name = models.CharField(max_length=100)
    crop_description = models.TextField()

    def __str__(self):
        return self.crop_name