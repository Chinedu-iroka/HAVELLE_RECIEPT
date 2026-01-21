from django.urls import path
from . import views

urlpatterns = [
    # This maps the invoice detail view
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
]