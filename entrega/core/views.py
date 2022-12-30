from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User