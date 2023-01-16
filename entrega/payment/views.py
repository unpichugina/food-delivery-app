import stripe
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from core.models import Product
from order.models import OrderItem, Order
from order.views import CreateOrder

from cart.models import Cart, CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY
SUCCESS_URL = "http://localhost:8000/payment/success/"
CANCEL_URL = "http://localhost:8000/payment/cancel/"


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        cart_item = CartItem.objects.all()
        # count the total of the order
        total_sum = 0
        for item in cart_item:
            total_sum += item.quantity * item.price

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
            return redirect(checkout_session.url)
        elif "pay_bonus" in request.POST:
            current_user = self.request.user
            if current_user.bonus < total_sum:
                return redirect(CANCEL_URL)
            current_user.bonus -= float(total_sum)
            current_user.save()
            return redirect(SUCCESS_URL)
        else:
            current_user = self.request.user
            current_user.bonus += round(float(total_sum) * 0.01, 2)
            current_user.save()
            return redirect(SUCCESS_URL)
