from django.contrib import admin
from .models import Customer, Merchant, PaymentMethod, Transaction, Refund, Payout, Invoice, Dispute

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "name", "email", "billing_address", "phone_number", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ("merchant_id", "name", "status", "default_currency", "created_at")
    list_filter = ("status", "default_currency", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = (
        "payment_method_id", "customer", "merchant",
        "method_type", "provider", "account_number",
        "expiry_date", "is_default", "created_at"
    )
    search_fields = ("customer__name", "merchant__name", "provider", "account_number")
    list_filter = ("method_type", "provider", "is_default", "created_at")
    ordering = ("-created_at",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_id", "merchant", "customer",
        "payment_method", "amount", "currency",
        "status", "created_at"
    )
    search_fields = ("transaction_id", "customer__name", "merchant__name")
    list_filter = ("status", "currency", "created_at")
    ordering = ("-created_at",)


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ("refund_id", "transaction", "amount", "status", "created_at")
    search_fields = ("refund_id", "transaction__transaction_id")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ("payout_id", "merchant", "amount", "currency", "status", "created_at")
    search_fields = ("payout_id", "merchant__name")
    list_filter = ("status", "currency", "created_at")
    ordering = ("-created_at",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", "customer", "merchant", "amount", "due_date", "created_at")
    search_fields = ("invoice_id", "customer__name", "merchant__name")
    list_filter = ("due_date", "created_at")
    ordering = ("-created_at",)


@admin.register(Dispute)
class DisputeAdmin(admin.ModelAdmin):
    list_display = ("dispute_id", "transaction", "reason", "status", "opened_at", "resolved_at")
    search_fields = ("dispute_id", "transaction__transaction_id", "reason")
    list_filter = ("status", "opened_at", "resolved_at")
    ordering = ("-opened_at",)