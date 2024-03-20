from django.urls import path

from main.views import *

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='home'),
    path('', LoginPageView.as_view(), name='login'),
    # products
    path('measure_unit/', MeasureUnitPageView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductPageView.as_view(), name='category_product'),
    path('indicator/', IndicatorPageView.as_view(), name='indicator'),
    path('product/', ProductPageView.as_view(), name='product'),
    # expense
    path('new-expense/', ExpenseCreateView.as_view(), name='new_expense')
]