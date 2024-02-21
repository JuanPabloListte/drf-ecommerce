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
            return Response({'message':'Product create successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)