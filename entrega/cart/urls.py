from django.urls import path
from cart import views

urlpatterns = [
    path('review/', views.CartView.as_view(), name='review'),
    path('add/', views.AddToCartView.as_view(), name='add_item_to_cart'),
]
