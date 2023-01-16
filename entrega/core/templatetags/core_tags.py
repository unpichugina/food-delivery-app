from django import template
from core.models import Product, Menu
from django.db.models import Sum

register = template.Library()


@register.inclusion_tag('includes/popular_list.html')
def get_popular_products():
    return {
        'product_list':  Product.objects.annotate(quantity_sum=Sum('orderitem__quantity')).order_by('-quantity_sum')[:8]
    }


@register.inclusion_tag('includes/popular_list.html')
def get_new_products():
    return {
        'product_list': Product.objects.all().order_by('-created_at')[:5]
    }

