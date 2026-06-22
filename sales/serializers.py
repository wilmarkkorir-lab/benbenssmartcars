from rest_framework import serializers
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    car_name = serializers.StringRelatedField(source='car', read_only=True)
    customer_name = serializers.StringRelatedField(source='customer', read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'

    def validate_sale_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Sale price must be greater than 0")
        return value

    def validate_car(self, value):
        if not value.is_available:
            raise serializers.ValidationError("This car is not available for sale")
        return value
