from django.urls import path
from order import views

urlpatterns = [
    path('confirmation/', views.CreateOrder.as_view(), name='confirmation_new'),
    path('history/', views.OrderHistoryView.as_view(), name='history'),
]
