from django.urls import path
from order import views

urlpatterns = [
    path('history/', views.OrderHistoryView.as_view(), name='history'),
]
