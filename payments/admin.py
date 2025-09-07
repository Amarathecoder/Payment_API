from django.contrib import admin
from .models import Merchant, Customer, Payment, Dispute
# Register your models here.

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ("merchant_id", "name", "status", "default_currency", "created_at")
    list_filter = ("status", "default_currency", "created_at")
    search_fields = ("name",)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "name", "email", "phone_number", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "merchant", "amount", "currency", "status", "created_at")
    search_fields = ("customer__name", "merchant__name")
    list_filter = ("status", "currency", "created_at")
    ordering = ("-created_at",)


@admin.register(Dispute)
class DisputeAdmin(admin.ModelAdmin):
    list_display = ("id", "payment", "reason", "resolved", "created_at")
    search_fields = ("payment__id", "reason")
    list_filter = ("resolved", "created_at")
    ordering = ("-created_at",)