from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateField()
    
    # Client Details
    client_name = models.CharField(max_length=100)
    client_address = models.TextField()
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField()
    
    # logo field we added in the previous step
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    # Payment Info
    bank_name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Invoice {self.invoice_number}"

    @property
    def get_subtotal(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def get_total(self):
        # Now Total is just the Subtotal
        return self.get_subtotal

class InvoiceItem(models.Model):
    # Links each item to a specific invoice
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity * self.unit_price