from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MerchantViewSet, CustomerViewSet, PaymentMethodViewSet, TransactionViewSet
from .views import RefundViewSet, PayoutViewSet, InvoiceViewSet, DisputeViewSet

# Create DRF router instance
router = DefaultRouter()

# Register all viewsets with API routes
router.register(r'merchants', MerchantViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'refunds', RefundViewSet)
router.register(r'payouts', PayoutViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'disputes', DisputeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
