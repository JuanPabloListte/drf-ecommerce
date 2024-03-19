from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from apps.expense_manager.api.serializers.expense_serializer import *
from apps.expense_manager.models import Supplier
from apps.expense_manager.api.serializers.general_serializer import SupplierSerializer


class ExpenseViewSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer
    
    @action(methods=['GET'], detail=False)
    def search_supplier(self, request):
        cuil_or_business_name = request.query_params.get('cuil_or_business_name')
        supplier = Supplier.objects.filter(
            Q(cuil__iexact=cuil_or_business_name) |
            Q(business_name__iexact=cuil_or_business_name)
        ).first()
        if supplier:
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data, status=status.HTTP_200_OK)
        return Response({
            'mensaje': 'Supplier not found.'
        }, status=status.HTTP_400_BAD_REQUEST)