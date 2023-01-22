from django.contrib.auth.models import AbstractUser
from django.db import models


def category_upload_path(self, file):
    return f'category/{self.id}/{file}'


def restaurant_upload_path(self, file):
    return f'restaurant/{self.id}/{file}'


def product_upload_path(self, file):
    return f'product/{self.section.id}/{file}'


class AppUser(AbstractUser):
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    bonus = models.FloatField(default=0)


class NameIt(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(NameIt):
    image = models.ImageField(upload_to=category_upload_path, default='new_category.png')


class RestaurantManager(models.Manager):

    def get_prefetched(self):
        return self.get_queryset().prefetch_related('tags')

    def get_by_category_id(self, category_id):
        return self.get_prefetched().filter(category=category_id)


class Restaurant(NameIt):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=restaurant_upload_path)
    tags = models.ManyToManyField("core.Tag")

    objects = RestaurantManager()


class Menu(NameIt):
    pass


class ProductManager(models.Manager):

    def get_prefetched(self):
        return self.get_queryset().select_related('section', 'restaurant')

    def get_by_restaurant_id(self, restaurant_id):
        return self.get_prefetched().filter(restaurant=restaurant_id)


class Product(NameIt):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    ingredient = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_price = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()


class ImageManager(models.Manager):

    def get_by_product_id(self, product_id):
        return self.get_queryset().filter(product=product_id)


class Image (models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'product/', blank=True)
    default = models.BooleanField(default=False)

    objects = ImageManager()


class Tag(NameIt):
    pass
