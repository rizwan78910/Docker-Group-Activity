from django.shortcuts import render

def landing(request):
    return render(request, 'shop/landing.html')

def cart(request):
    return render(request, 'shop/cart.html')

def checkout(request):
    return render(request, 'shop/checkout.html')
