from rest_framework import serializers
from .models import Merchant, Customer, PaymentMethod, Transaction, Refund, Payout, Invoice, Dispute


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.name", read_only=True)
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = PaymentMethod
        fields = [
            "payment_method_id",
            "customer",
            "customer_name",
            "merchant",
            "merchant_name",
            "type",
            "provider",
            "account_number",
            "expiry_date",
            "is_default",
            "status",
            "currency",
            "created_at"
        ]


class TransactionSerializer(serializers.ModelSerializer):
    merchant = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    # Change this to allow selection of payment methods
    payment_method = serializers.PrimaryKeyRelatedField(
        queryset=PaymentMethod.objects.all()
    )

    class Meta:
        model = Transaction
        fields = "__all__"


class RefundSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source="transaction.transaction_id", read_only=True)
    merchant_name = serializers.CharField(source="transaction.merchant.name", read_only=True)
    customer_name = serializers.CharField(source="transaction.customer.name", read_only=True)

    class Meta:
        model = Refund
        fields = [
            "refund_id",
            "transaction",
            "transaction_id",
            "merchant_name",
            "customer_name",
            "amount",
            "reason",
            "status",
            "created_at"
        ]


class PayoutSerializer(serializers.ModelSerializer):
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = Payout
        fields = [
            "payout_id",
            "merchant",
            "merchant_name",
            "amount",
            "currency",
            "status",
            "created_at"
        ]


class InvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.name", read_only=True)
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "invoice_id",
            "customer",
            "customer_name",
            "merchant",
            "merchant_name",
            "amount",
            "due_date",
            "created_at"
        ]


class DisputeSerializer(serializers.ModelSerializer):
    transaction_id = serializers.IntegerField(source="transaction.transaction_id", read_only=True)
    merchant_name = serializers.CharField(source="transaction.merchant.name", read_only=True)
    customer_name = serializers.CharField(source="transaction.customer.name", read_only=True)

    class Meta:
        model = Dispute
        fields = [
            "dispute_id",
            "transaction",
            "transaction_id",
            "merchant_name",
            "customer_name",
            "reason",
            "status",
            "opened_at",
            "resolved_at"
        ]