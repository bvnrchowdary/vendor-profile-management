# vendor_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendormodel')
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchaseordermodel')

urlpatterns = [
    path('', include(router.urls)),
]
