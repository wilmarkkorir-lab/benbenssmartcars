from django.db import models
from cars.models import Car
from customers.models import Customer


class Sale(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('installment', 'Installment'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='sale')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    sale_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car} sold to {self.customer}"
