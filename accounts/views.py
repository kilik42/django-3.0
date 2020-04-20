from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    

    total_orders = order.count()
    context = {'orders':customers, 'customers':customers,'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request):
    return render(request, 'accounts/customer.html')
