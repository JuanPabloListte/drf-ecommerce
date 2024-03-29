from apps.products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)
        
    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('You must enter a measure unit')
        return value
    
    def validate_category_product(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('You must enter a category product')
        return value
    
    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({'measure_unit':'You must enter a measure unit'})
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({'category_product':'You must enter a category product'})
        
        return data
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'stock': instance.stock.get('quantity__sum') if instance.stock.get('quantity__sum') is not None else 0,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image else None,
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }
        
        
class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')