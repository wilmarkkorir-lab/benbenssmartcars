from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['car', 'customer', 'sale_price', 'payment_method', 'sale_date']
    list_filter = ['payment_method']
