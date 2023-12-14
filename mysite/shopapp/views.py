
from django.db.models import Sum
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'shopapp/index.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'shopapp/products.html', context={'products': products})

def orders_list(request):
    all_orders = []

    orders = Order.objects.select_related('customer')

    for order in orders:
        order_products = order.orderproducts_set.all()
        print(order_products)

        products_list = [
            {
                'name': order_product.product.name,
                'count': order_product.count
            }
            for order_product in order_products
        ]

        all_orders.append(
            {
                'orderid': order.id,
                'customer': order.customer,
                'comment': order.comment,
                'date': order.date,
                'products': products_list
            }
        )

    return render(request, 'shopapp/orders.html', context={'orders': all_orders})