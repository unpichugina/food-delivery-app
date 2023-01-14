from django.contrib import admin
from cart import models

admin.site.register(models.Cart)
admin.site.register(models.CartItem)
