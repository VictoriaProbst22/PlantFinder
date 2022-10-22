from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
