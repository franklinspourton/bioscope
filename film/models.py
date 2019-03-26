from django.db import models

# Create your models here.

class Film(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    film_name = models.CharField(max_length=20, blank=False, unique=True)