from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response 
from apps.products.models import Indicator, MeasureUnit

class MeasureUnitViewSet(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.filter(state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
    
    def create(self, request):
        return Response({})
    

class IndicatorViewSet(viewsets.ViewSet):
    serializer_class = IndicatorSerializer
    model = Indicator
    
    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.filter(state=True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    
    
class CategoryProductViewSet(viewsets.ViewSet):
    serializer_class = CategoryProductSerializer
    
