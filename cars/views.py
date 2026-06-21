from rest_framework import viewsets, filters
from .models import Car, Category, CarImage
from .serializers import CarSerializer, CategorySerializer, CarImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(is_available=True).order_by('-created_at')
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brand', 'model', 'year', 'condition', 'category__name']
    ordering_fields = ['price', 'year', 'created_at']


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
