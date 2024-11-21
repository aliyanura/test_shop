from django.contrib import admin
from seller.models import Seller

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    list_filter = ("user",)
    fields = ('user', 'bio')

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
