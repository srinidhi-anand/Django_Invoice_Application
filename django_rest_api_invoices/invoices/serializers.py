from rest_framework import routers,serializers,viewsets
from .models import Invoice

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_id', 'invoice_number', 'customer_address', 'customer_city_state',  'customer_cntry', 'customer_name', 'date', 'customer_address', 'due_date',  'notes', 'salesperson_address', 'salesperson_company', 'salesperson_city_state', 'salesperson_cntry', 'customer_city_state',  'created_at', 'salesperson_name', 'status', 'subtotal', 'taxtotal',  'terms', 'total', 'line_items', 'created_at']