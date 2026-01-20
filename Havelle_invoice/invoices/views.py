from django.shortcuts import render, get_object_or_404
from .models import Invoice

# Create your views here.
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})
    
    def home(request):
    return render(request, 'invoices/home.html')