from django.shortcuts import render


def detect(request):
    return render(request,'option.html')

def product(request):
    return render(request, 'product.html')

def home(request):
    return render(request, 'index.html')
