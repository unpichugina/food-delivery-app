from django.urls import path, include
from core import views

urlpatterns = [
    path('review/', views.ProductView.as_view(), name='review'),
    path("<int:pk>/", views.MenuView.as_view(), name='menu'),
]