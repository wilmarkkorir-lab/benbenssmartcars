from rest_framework.routers import DefaultRouter
from .views import SaleViewSet

router = DefaultRouter()
router.register('sales', SaleViewSet)

urlpatterns = router.urls
