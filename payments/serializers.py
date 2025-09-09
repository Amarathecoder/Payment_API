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
    merchant = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    payment_method = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = "__all__"


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
