from django.contrib import admin
from .models import productinfo

# Register your models here.
class productinfoadmin(admin.ModelAdmin):
    list_display=['productname']

admin.site.register(productinfo,productinfoadmin)

