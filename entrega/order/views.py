from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from order.forms import OrderConfirmationForm
from cart.models import Cart, CartItem
from order.models import Order, OrderItem


class CreateOrder(FormView):
    template_name = 'order.html'
    form_class = OrderConfirmationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cart_item = CartItem.objects.all()
        order = form.save()
        for item in cart_item:
            OrderItem.objects.create(order=order,
                                     product=item.product,
                                     price=item.price,
                                     quantity=item.quantity)
        cart_item.delete()
        order.total = 0
        cart = Cart.objects.all()
        for item in cart:
            order.total += item.total
        order.save()
        cart.delete()
        # if order.payment == 'Cashless payment':
        #     return super(CreateOrder, self).form_valid(form)
        return super(CreateOrder, self).form_valid(form)


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'history.html'
    model = Order

    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            return self.model.objects.get_by_user_id(user_id)
        return super(OrderHistoryView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(OrderHistoryView, self).get_context_data(**kwargs)
        context['items'] = OrderItem.objects.all()
        return context


