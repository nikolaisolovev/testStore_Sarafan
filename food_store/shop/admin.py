from django.contrib import admin

from .models import Category, Subcategory, Product, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'subcategory', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'total_count')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'count', 'price')
