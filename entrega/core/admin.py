from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Restaurant)
admin.site.register(models.Ingredient)
admin.site.register(models.Tag)
admin.site.register(models.AppUser)
admin.site.register(models.Menu)
admin.site.register(models.Product)

