from django.contrib import admin
from product.models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    list_filter = ("name",)
    fields = ('name',)

    def has_add_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price', 'seller',)
    list_display_links = ("name",)
    list_filter = ("name", 'price', 'seller', 'categories')
    fields = ("name", 'description',
              'price', 'seller', 'categories')

    def has_add_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False
