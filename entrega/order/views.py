from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from order.models import Order, OrderItem


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


