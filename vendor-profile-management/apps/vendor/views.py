from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


    @action(methods=['GET'], url_path='performance', detail=True, permission_classes=[])
    def vendor_performance(self, request, pk):
        response = HistoricalPerformance.objects.filter(vendor_id=pk).first()
        if response:
            serializer = HistoricalPerformanceSerializer(instance=response)
            serialized_data = serializer.data

            return Response({'Success': True, 'Result': serialized_data},
                            status=status.HTTP_200_OK)
        else:
            return Response({'Success': False, 'Message': "Data not available."},
                            status=status.HTTP_404_NOT_FOUND)



class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


    @action(methods=['PATCH'], url_path='acknowledge', detail=True, permission_classes=[])
    def update_acknowledgment(self, request, pk):
        body = request.data
        acknowledgment_date = body.get('acknowledgment_date')
        try:
            purchase_order_obj = get_object_or_404(PurchaseOrder, vendor=pk)
            purchase_order_obj.acknowledgment_date = acknowledgment_date
            purchase_order_obj.save()
            return Response({'Success': True, 'Result': "Updated sucessfully."},
                        status=status.HTTP_200_OK)
        except Exception:
            return Response({'Success': False, 'Message': "data not available."},
                        status=status.HTTP_404_NOT_FOUND)
