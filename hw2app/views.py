from django.shortcuts import render
from .models import Client, Product, Order
import random
from django.http import HttpResponse



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
        order=Order(client=random.choice(clients),total_amount=0)
        num=random.randint(1,9)
        order.save()
        for i in range(num):
            order.products.add(random.choice(products))
        Order.calculate_total_amount(order)
        order.save()
    return HttpResponse('order')
            

    
