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
    path('category/', views.CategoryView.as_view(), name="category"),
    path('profile/', include(('core.urls.user_urls', 'core'), namespace='profile')),
    path("menu/", include(('core.urls.product_urls', 'core'), namespace='menu')),
    path("nav/", include(('core.urls.nav_urls','core'), namespace='nav')),

    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
