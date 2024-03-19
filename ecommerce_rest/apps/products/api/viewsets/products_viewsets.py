from apps.products.api.serializers.product_serializer import ProductSerializer, ProductRetrieveSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.base.utils import validate_files


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": product_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    
    def create(self, request):
        data = validate_files(request.data, 'image')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = ProductRetrieveSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'There is no product with this data!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            data = validate_files(request.data, 'image', True)
            product_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Product updated successfully!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully!'}, status=status.HTTP_200_OK)
        return Response({"error": "The selected product doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)

