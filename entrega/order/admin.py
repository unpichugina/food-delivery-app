from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
