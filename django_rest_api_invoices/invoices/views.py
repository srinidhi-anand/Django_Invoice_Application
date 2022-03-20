from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import InvoiceSerializer
from .models import Invoice

@csrf_exempt
def invoices(request):
    if(request.method == 'GET'):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = InvoiceSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def invoice_detail(request, invoice_id):
    try:
        invoices = Invoice.objects.get(invoice_id=str(invoice_id))
    except:
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        serializer = InvoiceSerializer(invoices, many=False)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = InvoiceSerializer(invoices, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

