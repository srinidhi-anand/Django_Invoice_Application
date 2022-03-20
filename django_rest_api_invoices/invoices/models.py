from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_id= models.CharField(max_length=100)
    invoice_number =  models.TextField()
    customer_address = models.TextField(blank=True)
    customer_city_state = models.TextField(blank=True)
    customer_cntry = models.TextField(blank=True)
    customer_name = models.TextField()
    date=  models.DateField()
    due_date=  models.DateField()
    notes = models.TextField(blank=True)
    salesperson_address = models.TextField(blank=True)
    salesperson_city_state = models.TextField(blank=True)
    salesperson_cntry = models.TextField(blank=True)
    salesperson_company = models.TextField(blank=True)
    salesperson_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    subtotal=  models.DecimalField( max_digits=19, decimal_places=2)
    taxtotal =  models.DecimalField( max_digits=19, decimal_places=2)
    terms = models.TextField(max_length=100,blank=True)
    total =  models.DecimalField( max_digits=19, decimal_places=2)
    line_items = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return the invoice id
        return self.invoice_id