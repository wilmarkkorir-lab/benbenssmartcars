from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import requests
import urllib.parse
from .models import Customer, Inquiry
from .serializers import CustomerSerializer, InquirySerializer


def send_whatsapp_notification(customer, inquiry):
    try:
        car_info = f"Car: {inquiry.car}" if inquiry.car else "General Inquiry"
        message = (
            f"🚗 *New Inquiry - BenBens Smart Cars*\n\n"
            f"👤 Name: {customer.name}\n"
            f"📧 Email: {customer.email}\n"
            f"📞 Phone: {customer.phone}\n"
            f"🏷️ {car_info}\n\n"
            f"💬 Message:\n{inquiry.message}\n\n"
            f"Reply to: {customer.phone}"
        )
        encoded_message = urllib.parse.quote(message)
        url = (
            f"https://api.callmebot.com/whatsapp.php"
            f"?phone={settings.WHATSAPP_PHONE}"
            f"&text={encoded_message}"
            f"&apikey={settings.WHATSAPP_API_KEY}"
        )
        response = requests.get(url, timeout=10)
        print(f"WhatsApp notification sent: {response.status_code}")
    except Exception as e:
        print(f"WhatsApp notification error: {e}")


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().order_by('-created_at')
    serializer_class = InquirySerializer

    def perform_create(self, serializer):
        inquiry = serializer.save()
        customer = inquiry.customer

        # Send WhatsApp notification
        send_whatsapp_notification(customer, inquiry)

        # Send email notification
        try:
            car_info = f"Car: {inquiry.car}" if inquiry.car else "General Inquiry"
            subject = f"New Inquiry from {customer.name} - BenBens Smart Cars"
            message = (
                f"New inquiry on BenBens Smart Cars!\n\n"
                f"From: {customer.name}\n"
                f"Email: {customer.email}\n"
                f"Phone: {customer.phone}\n"
                f"{car_info}\n\n"
                f"Message:\n{inquiry.message}\n\n"
                f"View in admin: https://benbenssmartcars.alwaysdata.net/admin/customers/inquiry/"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email notification error: {e}")
