from django.db import models

# Create your models here.

CURRENCY_CHOICES = [
    ('NGN', 'Nigerian Naira'),
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
    ('KES', 'Kenyan Shilling'),
    ('GHS', 'Ghanaian Cedi'),
]

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    billing_address = models.TextField(blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Merchant(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("blocked", "Blocked"),
    ]
    merchant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    default_currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default="NGN")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.default_currency})"


class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="payment_methods")
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="payment_methods")
    method_type = models.CharField(max_length=20)  # e.g. card, bank, mobile
    provider = models.CharField(max_length=20)    # e.g. Visa, Mastercard, PayPal
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="NGN")
    account_number = models.CharField(max_length=30)
    expiry_date = models.DateField(null=True, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method_type} ({self.provider})"


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="transactions")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="transactions")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="NGN") 
    status = models.CharField(max_length=20, default="pending", choices=[     # pending, success, failed, refunded
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Txn {self.transaction_id} - {self.status}"

class Refund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="refunds")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="NGN")
    reason = models.TextField() 
    status = models.CharField(max_length=20, default="initiated", choices=[     # initiated, completed, rejected
        ('INITIATED', 'Initiated'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund {self.refund_id} - {self.status}"
    
class Payout(models.Model):
    payout_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="payouts")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="NGN")
    status = models.CharField(max_length=20, default="processing", choices=[    # processing, completed, failed
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payout {self.payout_id} - {self.status}"

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="invoices")
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="invoices")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default="NGN")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.amount}"

class Dispute(models.Model):
    dispute_id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="disputes")
    reason = models.TextField()  
    status = models.CharField(max_length=20, default="open", choices=[   # open, resolved, rejected
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected')
    ])
    opened_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Dispute {self.dispute_id} - {self.status}"