

from django.db import models

# Create your models here.
class book(models.Model):
    Title=models.TextField()
    Author=models.CharField(max_length=30)
    Isbn=models.BigIntegerField()
    Publisher=models.CharField(max_length=30)