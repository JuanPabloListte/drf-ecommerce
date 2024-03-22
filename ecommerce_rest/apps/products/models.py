from django.db import models
from apps.base.models import BaseModel


class MeasureUnit(BaseModel):

    description = models.CharField('Description', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = "Measure Unit"
        verbose_name_plural = "Measure Units"

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField('Description', max_length=50, blank=False, unique=True, null=False)

    class Meta:
        verbose_name = "Category Product"
        verbose_name_plural = "Category Products"

    def __str__(self):
        return self.description
    
class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Supply Indicator')

    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"

    def __str__(self):
        return f'Category Offer: {self.category_product}, Discount: {self.discount_value}%' 


class Product(BaseModel):

    name = models.CharField('Product Name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product Description', blank=False, null=False)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)    
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Category Product', null=True)
    
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    @property
    def stock(self):
        from django.db.models import Sum
        from apps.expense_manager.models import Expense
        
        expenses = Expense.objects.filter(
            product=self,
            state=True
        ).aggregate(Sum('quantity'))
        
        return expenses