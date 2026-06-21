from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CategoryViewSet, CarImageViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)
router.register('categories', CategoryViewSet)
router.register('car-images', CarImageViewSet)

urlpatterns = router.urls
