from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response 
from apps.products.models import Indicator, MeasureUnit, CategoryProduct


class MeasureUnitViewSet(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Measure Unit registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Measure Unit updated successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Measure Unit deleted successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Measure Unit not found!'}, status=status.HTTP_400_BAD_REQUEST)
    

class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer
    model = Indicator
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Inidicator registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Inidicator updated successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Inidicator deleted successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Inidicator not found!'}, status=status.HTTP_400_BAD_REQUEST)

    
    
class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer
    model = CategoryProduct
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Category registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    # def retrieve(self, request, pk=None):
    #     if self.get_object().exists():
    #         data = self.get_object().get()
    #         data = self.get_serializer(data)
    #         return Response(data.data)
    #     return Response({'message':'', 'error':'Category not found!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Category updated successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Category deleted successfully!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Category not found!'}, status=status.HTTP_400_BAD_REQUEST)
    
