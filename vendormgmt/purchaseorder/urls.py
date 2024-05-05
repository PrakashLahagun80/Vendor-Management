# urls.py
from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-retrieve-update-destroy'),
]
