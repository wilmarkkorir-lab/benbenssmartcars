from rest_framework import serializers
from .models import Customer, Inquiry


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required")
        return value.strip()

    def validate_phone(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Phone is required")
        digits = value.strip().replace('+', '').replace('-', '').replace(' ', '')
        if not digits.isdigit() or not (7 <= len(digits) <= 15):
            raise serializers.ValidationError("Enter a valid phone number")
        return value.strip()


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

    def validate_message(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Message cannot be empty")
        return value.strip()
