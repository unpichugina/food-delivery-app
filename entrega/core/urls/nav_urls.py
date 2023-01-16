from django.urls import path, include
from core import views

urlpatterns = [
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path("contact/", views.ContactView.as_view(), name='contact'),
    path("delivery/", views.DeliveryView.as_view(), name='delivery'),
    path("payment/", views.PaymentView.as_view(), name='payment'),
]