from django import template
from core.models import Product, Menu
from django.shortcuts import render

register = template.Library()


@register.inclusion_tag('includes/product_list.html')
def get_popular_products():
    return {
        'product_list': Product.objects.all().order_by('price')[:5]
    }

