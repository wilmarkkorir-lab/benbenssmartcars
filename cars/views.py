from rest_framework import viewsets, filters
from .models import Car, Category, CarImage
from .serializers import CarSerializer, CategorySerializer, CarImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brand', 'model', 'year', 'condition', 'category__name']
    ordering_fields = ['price', 'year', 'created_at']

    def get_queryset(self):
        queryset = Car.objects.all().order_by('-created_at')
        available = self.request.query_params.get('is_available')
        if available is None:
            queryset = queryset.filter(is_available=True)
        return queryset


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
