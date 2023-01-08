from django.contrib.auth import get_user_model
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


class NameIt(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(NameIt):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=category_upload_path, default='new_category.png')

    def __str__(self):
        return self.name


class RestaurantManager(models.Manager):

    def get_prefetched(self):
        return self.get_queryset().prefetch_related('tags')

    def get_by_category_id(self, category_id):
        return self.get_prefetched().filter(category=category_id)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=restaurant_upload_path)
    tags = models.ManyToManyField("core.Tag")
    # menu = models.ForeignKey('core.Menu', on_delete=models.SET_NULL, null=True)
    objects = RestaurantManager()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):

    def get_prefetched(self):
        return self.get_queryset().select_related('section').prefetch_related('ingredient')

    def get_by_section_id(self, section_id):
        return self.get_queryset().filter(section=section_id)

    def get_by_restaurant_id(self, restaurant_id):
        return self.get_queryset().filter(restaurant=restaurant_id)


class Product(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=product_upload_path)
    description = models.TextField(max_length=1000, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredient = models.ManyToManyField("core.Ingredient", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# class Tag(NameIt):
#     pass

