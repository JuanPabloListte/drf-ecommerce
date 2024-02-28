from rest_framework.routers import DefaultRouter
from ecommerce_rest.apps.products.api.views.products_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls