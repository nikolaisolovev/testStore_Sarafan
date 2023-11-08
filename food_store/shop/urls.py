from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
   CategoriesWithSubcategoriesList,
   ProductViewSet,
   CartViewSet,
   CartItemViewSet,
)

router = DefaultRouter()

router.register(r'categories', CategoriesWithSubcategoriesList)
router.register(r'products', ProductViewSet)
router.register('cart', CartViewSet)
router.register(
   r'cart/(?P<cart_id>\d+)/cart_item',
   CartItemViewSet, basename='cart_item'
)


urlpatterns = [
   path('', include(router.urls)),
]
