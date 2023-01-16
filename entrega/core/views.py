from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, ListView, UpdateView
from core.forms import RegistrationForm
from core.models import Restaurant, Category, Product, Menu, Image
from order.models import Order, OrderItem


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['orders'] = Order.objects.all()
        context['details'] = OrderItem.objects.all()
        return context


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user = authenticate(self.request, username=user.username, password=form.cleaned_data['password'])
        login(request=self.request, user=user)
        return super(RegistrationView, self).form_valid(form)


class EditAppUserView(UpdateView):
    template_name = 'registration.html'
    model = get_user_model()
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'user_id'


class RestaurantView(ListView):
    template_name = 'restaurant.html'
    model = Restaurant
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.get_prefetched()


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


class ProductDetailView(DetailView):
    template_name = 'includes/product.html'
    model = Product

    def get_queryset(self):
        product_id = self.request.GET.get('id', None)
        if product_id:
            return self.model.objects.get_by_product_id(product_id)
        return super(ProductDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context


class PopularProductView(ListView):
    template_name = 'popular_list.html'
    model = Product


class AboutUsView(TemplateView):
    template_name = 'includes/reconstruction.html'
    model = Product


class ContactView(AboutUsView):
    pass


class DeliveryView(AboutUsView):
    pass


class PaymentView(AboutUsView):
    pass
