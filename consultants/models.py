from django.db import models

# Create your models here.
class Consultant(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='consultants/')

    def __str__(self):
        return self.name