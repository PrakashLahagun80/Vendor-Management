from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vendor
from purchaseorder.models import PurchaseOrder
from .serializers import VendorSerializer,VendorPerformanceSerializer


class VendorListCreateAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)


class AcknowledgePurchaseOrderAPIView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"message": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        purchase_order.status = 'acknowledged'
        purchase_order.save()
        return Response({"message": "Purchase Order acknowledged successfully"})