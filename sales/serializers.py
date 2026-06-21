from rest_framework import serializers
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    car_name = serializers.StringRelatedField(source='car', read_only=True)
    customer_name = serializers.StringRelatedField(source='customer', read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'
