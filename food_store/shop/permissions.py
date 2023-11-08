from rest_framework import permissions

from .models import Cart


class IsCartOwner(permissions.BasePermission):
    """Разрешено только владельцу корзины (действия с корзиной)."""
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user


class IsCartOwnerForCartItems(permissions.BasePermission):
    """Разрешено только владельцу корзины (действия с продуктами в корзине)."""
    def has_permission(self, request, view):
        cart = Cart.objects.get(id=view.kwargs.get('cart_id'))
        return cart.customer == request.user
