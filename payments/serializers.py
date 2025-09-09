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
    customer = serializers.StringRelatedField()
    merchant = serializers.StringRelatedField()

    class Meta:
        model = PaymentMethod
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)
    customer_name = serializers.CharField(source="customer.name", read_only=True)
    payment_method_type = serializers.CharField(source="payment_method.type", read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "transaction_id",
            "merchant",
            "merchant_name",      # Readable name
            "customer",
            "customer_name",      # Readable name
            "payment_method",
            "payment_method_type", # Readable type
            "amount",
            "currency",
            "status",
            "created_at"
        ]

        
class RefundSerializer(serializers.ModelSerializer):
    transaction = serializers.StringRelatedField()

    class Meta:
        model = Refund
        fields = "__all__"


class PayoutSerializer(serializers.ModelSerializer):
    merchant = serializers.StringRelatedField()

    class Meta:
        model = Payout
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    merchant = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        fields = "__all__"


class DisputeSerializer(serializers.ModelSerializer):
    transaction = serializers.StringRelatedField()

    class Meta:
        model = Dispute
        fields = "__all__"
