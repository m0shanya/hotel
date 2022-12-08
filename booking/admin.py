from django.contrib import admin

from booking.models import Rooms, Order


class PurchaseInline(admin.TabularInline):
    model = Order
    raw_id_fields = ['purchase']


@admin.register(Rooms)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "cost")
    search_fields = ("title",)
    inlines = [
        PurchaseInline,
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'paid',
                    'created_at', 'updated']
    list_filter = ['paid', 'created_at', 'updated']
