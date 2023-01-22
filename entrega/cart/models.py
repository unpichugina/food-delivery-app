from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


class Cart(models.Model):
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    token = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    note = models.TextField(blank=True, default='')
    total = models.DecimalField(default=0, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('core.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.product.name
