from django.urls import path 
from invoices import views

# define the urls
urlpatterns = [
    path('invoices/', views.invoices),
    path('invoices/<invoice_id>/', views.invoice_detail),
]