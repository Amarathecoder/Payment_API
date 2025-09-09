from rest_framework import viewsets, status
from .models import Merchant, Customer, PaymentMethod, Transaction, Refund, Payout, Invoice, Dispute
from .serializers import MerchantSerializer, CustomerSerializer, PaymentMethodSerializer, TransactionSerializer
from .serializers import RefundSerializer, PayoutSerializer, InvoiceSerializer, DisputeSerializer
import requests
from decimal import Decimal
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
def home(request):
    return JsonResponse({
        "message": "Welcome to the Payment API!",
        "api_root": "/api/"
    })

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        transaction = serializer.save()
        merchant_currency = transaction.merchant.default_currency
        customer_currency = transaction.original_currency

        # Fetch conversion if currencies differ
        if customer_currency != merchant_currency:
            try:
                url = f"https://api.exchangerate-api.com/v4/latest/{customer_currency}"
                response = requests.get(url)
                data = response.json()

                # Get the exchange rate, fallback to 1 if not found
                exchange_rate = Decimal(data["rates"].get(merchant_currency, 1))

                # Calculate converted amount
                converted_amount = transaction.amount * exchange_rate

                # Save conversion details
                transaction.converted_amount = converted_amount
                transaction.converted_currency = merchant_currency
                transaction.exchange_rate = exchange_rate

            except Exception:
                # If API fails, fallback to original amount & currency
                transaction.converted_amount = transaction.amount
                transaction.converted_currency = customer_currency
                transaction.exchange_rate = Decimal("1.0")
        else:
            transaction.converted_amount = transaction.amount
            transaction.converted_currency = merchant_currency
            transaction.exchange_rate = Decimal("1.0")

        # Simulate gateway payment outcome
        from random import choice
        transaction.status = choice(["SUCCESS", "FAILED", "PENDING"])
        transaction.save()


class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer


class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class DisputeViewSet(viewsets.ModelViewSet):
    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer

    def perform_update(self, serializer):
        dispute = serializer.save()

        # If dispute resolved and customer wins → auto-refund
        if dispute.status == "RESOLVED" and not dispute.resolved_at:
            dispute.resolved_at = timezone.now()
            dispute.save()

            transaction = dispute.transaction

            # Check if transaction wasn't refunded already
            existing_refund = Refund.objects.filter(transaction=transaction).first()
            if not existing_refund:
                Refund.objects.create(
                    transaction=transaction,
                    amount=transaction.amount,
                    reason=f"Auto-refund for dispute {dispute.dispute_id}",
                    status="INITIATED"
                )

                # Update transaction status
                transaction.status = "REFUNDED"
                transaction.save()