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
        params = self.request.query_params

        available = params.get('is_available')
        if available is None:
            queryset = queryset.filter(is_available=True)
        elif available.lower() in ('true', '1'):
            queryset = queryset.filter(is_available=True)
        elif available.lower() in ('false', '0'):
            queryset = queryset.filter(is_available=False)

        category = params.get('category')
        if category:
            queryset = queryset.filter(category__id=category)

        condition = params.get('condition')
        if condition:
            queryset = queryset.filter(condition=condition)

        price_min = params.get('price_min')
        if price_min:
            queryset = queryset.filter(price__gte=price_min)

        price_max = params.get('price_max')
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
