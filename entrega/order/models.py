from django.contrib.auth import get_user_model
from django.db import models

order_status = ((0, 'In Progress'), (1, 'Fulfilled'))


class OrderManager(models.Manager):

    def get_prefetched(self):
        return self.get_queryset().select_related('user')

    def get_by_user_id(self, user_id):
        return self.get_prefetched().filter(user=user_id)


class Order(models.Model):
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    note = models.TextField(blank=True, default='')
    status = models.IntegerField(choices=order_status, default=0)
    total = models.DecimalField(default=0, max_digits=100, decimal_places=2)

    objects = OrderManager()

    def __str__(self):
        return self.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('core.Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
