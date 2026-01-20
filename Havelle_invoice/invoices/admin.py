from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('invoice_number', 'client_name', 'is_paid', 'get_total', 'view_invoice')
    list_editable = ('is_paid',)
    search_fields = ('invoice_number', 'client_name')


# 2. Define the 'view_invoice' function
    def view_invoice(self, obj):
        # This creates a URL to the 'invoice_detail' view we made earlier
        url = reverse('invoice_detail', args=[obj.id])
        return format_html(
            '<a href="{}" target="_blank" style="'
            'background-color: #00203F; '
            'color: white; '
            'padding: 5px 15px; '
            'border-radius: 4px; '
            'text-decoration: none; '
            'font-weight: bold;">View</a>',
            url
        )

    view_invoice.short_description = 'Action' # Sets column header name