from django.contrib import admin
from .models import Car, Category, CarImage

admin.site.register(Category)
admin.site.register(CarImage)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'condition', 'is_available']
    list_filter = ['condition', 'is_available', 'category']
    search_fields = ['brand', 'model']
