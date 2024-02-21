from rest_framework import generics
from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer
    
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Product created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully!'}, status=status.HTTP_200_OK)
        return Response({"error": "The selected product doesn't exist."}, status=status.HTTP_400_BAD_REQUEST)