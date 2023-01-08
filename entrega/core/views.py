from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, FormView, ListView
from core.forms import RegistrationForm
from core.models import Restaurant, Category, Product, Menu


class IndexView(TemplateView):
    template_name = 'index.html'
    # model = Restaurant
    #
    # def get_queryset(self):
    #     return self.model.objects.get_prefetched()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user = authenticate(self.request, username=user.username, password=form.cleaned_data['password'])
        login(request=self.request, user=user)
        return super(RegistrationView, self).form_valid(form)


class RestaurantView(ListView):
    template_name = 'restaurant.html'
    model = Restaurant
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.get_prefetched()


# если поменять здесь на индекс вью будет фильтр прямо на главной
class CategoryView(RestaurantView):

    def get_queryset(self):
        category_id = self.request.GET.get('id', None)
        if category_id:
            return self.model.objects.get_by_category_id(category_id)
        return super(CategoryView, self).get_queryset()


class ProductView(ListView):
    template_name = 'menu.html'
    model = Product

    def get_queryset(self):
        restaurant_id = self.request.GET.get('id', None)
        if restaurant_id:
            return self.model.objects.get_by_restaurant_id(restaurant_id)
        return super(ProductView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        context['sections'] = Menu.objects.all()
        return context


class MenuView(ProductView):

    def get_queryset(self):
        section_id = self.request.GET.get('id', None)
        if section_id:
            return self.model.objects.get_by_section_id(section_id)
        return super(MenuView, self).get_queryset()





