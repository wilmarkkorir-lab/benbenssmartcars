from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, InquiryViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('inquiries', InquiryViewSet)

urlpatterns = router.urls
