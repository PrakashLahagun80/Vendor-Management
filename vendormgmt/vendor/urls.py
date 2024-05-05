# urls.py
from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDeleteAPIView, VendorPerformanceAPIView, AcknowledgePurchaseOrderAPIView


urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', VendorRetrieveUpdateDeleteAPIView.as_view(), name='vendor-retrieve-update-delete'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor_performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge_purchase_order'),
]
