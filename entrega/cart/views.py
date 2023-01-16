from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from cart.models import Cart, CartItem
from core.models import Product
from django.views.generic import View, ListView


class CartView(ListView):
    template_name = 'cart.html'
    model = CartItem

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['cart_details'] = Cart.objects.all()
        return context


class AddToCartView(View):
    http_methods = ['post']

    def post(self, request):
        product = get_object_or_404(Product, id=request.POST['product_id'])
        cart, created = Cart.objects.get_or_create(user=request.user, email=request.user.email)
        instance = CartItem.objects.filter(cart=cart, product=product)
        if instance.exists():
            cart_item = instance[0]
            cart_item.quantity += 1
            cart_item.price = cart_item.quantity * cart_item.product.price
            cart_item.save()
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, quantity=1, price=product.price)
        cart.total = 0
        cart_qs = CartItem.objects.all()
        for item in cart_qs:
            cart.total += item.price
        cart.save()
        return JsonResponse({'status': 'success'}, safe=False)
