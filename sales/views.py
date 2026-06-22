from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-sale_date')
    serializer_class = SaleSerializer

    def perform_create(self, serializer):
        sale = serializer.save()
        sale.car.is_available = False
        sale.car.save()
