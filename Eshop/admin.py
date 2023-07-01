# Register your models here.

from django.contrib import admin

from Eshop.models import CustomUser, Company, VideoGame, DigitalCode, Order, Payment


# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website",)
    list_filter = ("country",)


admin.site.register(Company, CompanyAdmin)


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name",)
    list_filter = ("is_active",)


admin.site.register(CustomUser, CustomerUserAdmin)


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ("title", "genre",)
    list_filter = ("price", "company", "platform",)
    search_fields = ("title__startswith", "genre__startswith",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(VideoGame, VideoGameAdmin)


class DigitalCodeAdmin(admin.ModelAdmin):
    list_display = ("videogame", "code_value", "status")
    list_filter = ("date_of_creation", "status")
    search_fields = ("code_value__startswith",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(DigitalCode, DigitalCodeAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_date", "order_status")
    list_filter = ("order_date", "order_status",)
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False


admin.site.register(Order, OrderAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "payment_date", "user",)
    list_filter = ("payment_date", "payment_method",)

    def has_add_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True


admin.site.register(Payment, PaymentAdmin)
