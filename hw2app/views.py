from django.shortcuts import render
from .models import Client, Product, Order
import random
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta



# Create your views here.
def facke_data(request):
    products=[]
    clients=[]
    article = ['торт','колбаса','хлеб','молоко','масло','чай','картофель','помидор']
    for i in range(30):
        product=Product(name=random.choice(article), description='Очень хороший товар', price=random.randint(1,10), quantity=random.randint(1,4))
        product.save()
        products.append(product)
    
    
    client_rand=['Мария','Петр','Антон','Елизавета','Михаил','Марина','Яна']
    adress=['ул.Ленина, 56','ул. Курская, 83','ул. Красная, 147','проспект Вернадского,1','проезд Ветеранов, 16']
    for i in range(10):
        client= Client(name=random.choice(client_rand), email=f'client{i}@mail.ru', phone_number=random.randint(6587456,9865656), address=random.choice(adress))
        client.save()
        clients.append(client)
    


    for i in range(15):
        order=Order(client=random.choice(clients),total_amount=0, order_date='2022-06-25')
        num=random.randint(1,9)
        order.save()
        for i in range(num):
            order.products.add(random.choice(products))
        Order.calculate_total_amount(order)
        order.save()

    for i in range(1,47):
        person=Order.objects.get(id=i)
        person.delete()

    return HttpResponse('order')

def index(request):
    """Главная страница."""
    return render(request, 'base.html')


def clients_list(request):
    """Список клиентов."""
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'client.html', context)


def client_orders(request, client_id):
    client_change = Client.objects.get(pk=client_id)
    client_orders_all=Order.objects.filter(client=client_change).all()
    set_order=[]
    for i in client_orders_all:
        set_order_item=i.products.all().distinct()
        for k in set_order_item:
            set_order.append(k)
            
    context = {
        'client_name': client_change.name,
        'client_orders_all': set(set_order),
        'client_id':client_change.id,
    }
    return render(request, 'order.html', context)

def client_orders_day(request, client_id):
    client_change = Client.objects.get(pk=client_id)
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Order.objects.filter(client=client_change, order_date__gte=last_7_days).all()
    set_order1=[]
    for i in client_orders_last_7_days:
        set_order_item=i.products.all().distinct()
        for k in set_order_item:
            set_order1.append(k)
    
    
    context = {
        'client_name': client_change.name,    
        'client_orders_last_7_days': set(set_order1),
        
    }
    return render(request, 'order_day.html', context)

            

def client_orders_mounth(request, client_id):
    client_change = Client.objects.get(pk=client_id)
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Order.objects.filter(client=client_change, order_date__gte=last_30_days).all()
    set_order2=[]
    for i in client_orders_last_30_days:
        set_order_item=i.products.all().distinct()
        for k in set_order_item:
            set_order2.append(k)
    print(set_order2)
    context = {
        'client_name': client_change.name,    
        'client_orders_last_30_days': set(set_order2),
        
    }
    return render(request, 'order_mounth.html', context)   

def client_orders_year(request, client_id):
    client_change = Client.objects.get(pk=client_id)
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Order.objects.filter(client=client_change, order_date__gte=last_365_days).all()
    set_order3=[]
    for i in client_orders_last_365_days:
        set_order_item=i.products.all().distinct()
        for k in set_order_item:
            set_order3.append(k)
    context = {
        'client_name': client_change.name,    
        'client_orders_last_365_days': set(set_order3),
        
    }
    return render(request, 'order_year.html', context)   