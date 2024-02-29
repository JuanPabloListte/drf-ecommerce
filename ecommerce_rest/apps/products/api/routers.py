from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_viewsets import ProductViewSet
from apps.products.api.views.general_views import (
    MeasureUnitViewSet,
    IndicatorViewSet,
    CategoryProductViewSet
)

router = DefaultRouter()

router.register(r'products',ProductViewSet, basename = 'products')
router.register(r'measure_unit', MeasureUnitViewSet, basename='measure_unit')
router.register(r'indicators', IndicatorViewSet, basename='indicators')
router.register(r'category_products', CategoryProductViewSet, basename='category_products')


urlpatterns = router.urls