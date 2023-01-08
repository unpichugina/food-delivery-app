"""entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='home'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('category/', views.CategoryView.as_view(), name="category"),
    # path('restaurant/', include(('core.urls.restaurant_urls', 'core'), namespace='restaurant')),
    path("restaurant/", include(('core.urls.menu_urls', 'core'), namespace='menu')),
    # path("menu/", views.ProductView.as_view(), name='menu'),
    path('section/', views.MenuView.as_view(), name="section"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
