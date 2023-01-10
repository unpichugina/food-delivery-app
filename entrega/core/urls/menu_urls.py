from django.urls import path, include
from core import views

urlpatterns = [
    path('review/', views.ProductView.as_view(), name='review'),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name='detail'),
]