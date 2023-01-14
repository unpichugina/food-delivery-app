from django.contrib import admin
from core import models
from core.models import Image


class ProductImagesInline(admin.StackedInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'restaurant', 'price', 'created_at', 'updated_at']
    search_fields = ['id', 'name', 'section', 'restaurant']
    list_filter = ['section', 'restaurant', 'created_at', 'updated_at']
    list_editable = ['price']
    inlines = [ProductImagesInline]


admin.site.register(models.Category)
admin.site.register(models.Restaurant)
admin.site.register(models.Tag)
admin.site.register(models.AppUser)
admin.site.register(models.Menu)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Image)