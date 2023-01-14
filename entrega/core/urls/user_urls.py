from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('review/', views.ProfileView.as_view(), name='review'),
    path("<int:user_id>/edit/", views.EditAppUserView.as_view(), name='edit'),
]
