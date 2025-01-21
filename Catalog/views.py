from django.shortcuts import render

# Create your views here.
def index(request):
    products = [
        {"name": "Смартфон", "price": 15000},
        {"name": "Ноутбук", "price": 55000},
        {"name": "Планшет", "price": 25000},
    ]
    return render(request, 'catalog/index.html', {'products': products})