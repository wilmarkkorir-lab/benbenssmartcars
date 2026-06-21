from rest_framework import serializers
from .models import Car, Category, CarImage
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
    
    def validate_year(self, value):
        current_year = datetime.now().year
        if value < 1900 or value > current_year + 1:
            raise serializers.ValidationError(f"Year must be between 1900 and {current_year + 1}")
        return value
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value
    
    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError("Mileage cannot be negative")
        return value
    
    def validate_brand(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Brand is required")
        return value.strip()
    
    def validate_model(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Model is required")
        return value.strip()
