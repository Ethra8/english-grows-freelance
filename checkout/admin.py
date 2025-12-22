from django.contrib import admin

from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('user_profile', 'order_number', 'date', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('user_profile', 'order_number', 'date', 'full_name',
              'email', 'order_total', 'grand_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'user_profile', 'full_name',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
