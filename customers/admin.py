from django.contrib import admin
from .models import Customer, Inquiry

admin.site.register(Customer)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car', 'created_at', 'is_resolved']
    list_filter = ['is_resolved']
