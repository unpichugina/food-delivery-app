import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from order.models import OrderItem, Order
from order.forms import OrderConfirmationForm


from cart.models import Cart, CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY
SUCCESS_URL = "http://localhost:8000/payment/success/"
CANCEL_URL = "http://localhost:8000/payment/cancel/"


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class CreateCheckoutSessionView(FormView):
    template_name = 'order.html'
    form_class = OrderConfirmationForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        cart_item = CartItem.objects.all()
        total_price = 0
        form = OrderConfirmationForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
        for item in cart_item:
            total_price += item.quantity * item.price
            OrderItem.objects.create(order=order,
                                     product=item.product,
                                     price=item.price,
                                     quantity=item.quantity)
        order.total = 0
        cart = Cart.objects.all()
        for item in cart:
            order.total += item.total
        order.save()
        cart.delete()

        if "pay_card" in request.POST:
            line_items = []
            for item in cart_item:
                line_items.append({
                    'price': item.product.stripe_price,
                    'quantity': item.quantity,
                })
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=SUCCESS_URL,
                cancel_url=CANCEL_URL,
            )
            cart_item.delete()
            return redirect(checkout_session.url)
        elif "pay_bonus" in request.POST:
            current_user = self.request.user
            if current_user.bonus < total_price:
                return redirect(CANCEL_URL)
            current_user.bonus -= float(total_price)
            current_user.save()
            cart_item.delete()
            return redirect(SUCCESS_URL)
        else:
            current_user = self.request.user
            current_user.bonus += round(float(total_price) * 0.01, 2)
            current_user.save()
            cart_item.delete()
            return redirect(SUCCESS_URL)

    def get_context_data(self, **kwargs):
        context = super(CreateCheckoutSessionView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['form'] = OrderConfirmationForm(
                initial={'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name,
                         'email': user.email, 'phone': user.phone, 'address': user.address}
            )
        return context

