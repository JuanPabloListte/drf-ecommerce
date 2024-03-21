from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from apps.expense_manager.api.serializers.expense_serializer import *
from apps.expense_manager.models import Supplier, Voucher, PaymentType
from apps.expense_manager.api.serializers.general_serializer import *
from apps.products.models import Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.base.utils import format_date

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
        
    @action(methods=['POST'], detail=False)
    def new_supplier(self, request):
        data_supplier = request.data
        data_supplier = SupplierRegisterSerializer(data=data_supplier)
        if data_supplier.is_valid():
            data_supplier = data_supplier.save()
            return Response({
                'message': 'Provider registered successfully',
                'supplier': data_supplier
            }, status=status.HTTP_201_CREATED)
        return Response({'error': data_supplier.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(methods=['GET'], detail=False)
    def get_vouchers(self, request):
        data = Voucher.objects.filter(state=True).order_by('id')
        data = VoucherSerializer(data, many=True).data
        return Response(data)
    
    @action(methods=['GET'], detail=False)
    def get_payment_types(self, request):
        data = PaymentType.objects.filter(state=True).order_by('id')
        data = PaymentTypeSerializer(data, many=True).data
        return Response(data)
    
    @action(methods=['GET'], detail=False)
    def get_products(self, request):
        data = Product.objects.filter(state=True).order_by('id')
        data = ProductSerializer(data, many=True).data
        return Response(data)
    
    def format_data(self, data):
        JWT_auth = JWTAuthentication()
        user, _ = JWT_auth.authenticate(self.request)
        data['user'] = user.id
        data['date'] = format_date(data['date'])
        return data
    
    def create(self, request):
        data = self.format_data(request.data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Invoice successfully registered'}, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error registering the invoice',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)