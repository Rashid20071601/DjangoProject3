from django.shortcuts import render, redirect

# Create your views here.
# Пример данных (товары с категориями)
products = [
    {'id': 1, 'name': 'Смартфон Samsung Galaxy', 'category': 'телефоны', 'price': 15000},
    {'id': 2, 'name': 'Планшет Apple iPad', 'category': 'планшеты', 'price': 45000},
    {'id': 3, 'name': 'Наушники Sony WH-1000XM4', 'category': 'аксессуары', 'price': 25000},
    {'id': 4, 'name': 'Ноутбук Dell XPS 13', 'category': 'ноутбуки', 'price': 95000},
    {'id': 5, 'name': 'Смарт-часы Xiaomi Mi Band', 'category': 'аксессуары', 'price': 3000},
]


def index(request):
    return render(request, 'catalog/index.html', {'products': products})


def product_list(request):
    # Получаем параметр 'category' из строки запроса
    category = request.GET.get('category')

    # Если категория указана, фильтруем товары
    if category:
        filtered_products = [product for product in products if product['category']==category]
    else:
        filtered_products = products

    return render(request, 'catalog/product_list.html', {'products': filtered_products})


def add_product(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')

        # Добавляем новый товар в список
        products.append({
            'id': len(products)+1,
            'name': name,
            'category': category,
            'price': int(price)
        })

        # Перенаправляем на список товаров
        return redirect('product_list')   # Имя маршрута списка товаров

    # Если GET-запрос, отображаем форму
    return render(request, 'catalog/add_product.html')