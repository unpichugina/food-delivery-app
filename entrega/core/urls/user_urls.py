from django.urls import path, include
from core import views

urlpatterns = [
    path('review/', views.ProfileView.as_view(), name='review'),
    path("<int:user_id>/edit/", views.EditAppUserView.as_view(), name='edit'),
]
