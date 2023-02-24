from django.db import models


# Create your models here.
class productinfo (models.Model):
    productname=models.CharField(max_length=20)