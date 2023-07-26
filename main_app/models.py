from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
