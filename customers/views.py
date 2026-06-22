from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer, Inquiry
from .serializers import CustomerSerializer, InquirySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().order_by('-created_at')
    serializer_class = InquirySerializer

    def perform_create(self, serializer):
        inquiry = serializer.save()
        # Send email notification
        try:
            customer = inquiry.customer
            car_info = f"Car: {inquiry.car}" if inquiry.car else "General Inquiry"
            subject = f"New Inquiry from {customer.name} - BenBens Smart Cars"
            message = f"""
You have a new inquiry on BenBens Smart Cars!

----------------------------
From: {customer.name}
Email: {customer.email}
Phone: {customer.phone}
{car_info}

Message:
{inquiry.message}
----------------------------

Reply directly to: {customer.email}
or WhatsApp: {customer.phone}

View in admin: https://benbenssmartcars.alwaysdata.net/admin/customers/inquiry/
            """
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email notification error: {e}")
