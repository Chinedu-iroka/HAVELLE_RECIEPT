from django.shortcuts import render, get_object_or_404
from .models import Invoice
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})
    
def home(request):
    return render(request, 'invoices/invoice_detail.html')


def create_initial_superuser(request):
    User = get_user_model()
    # Replace 'admin' and 'your_password' with your preferred login details
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='havelle',
            email='lifestroglobal@gmail.com',
            password='dsdA13$%^&&' 
        )
        return HttpResponse('Superuser created successfully!')
    else:
        return HttpResponse('Superuser already exists.')