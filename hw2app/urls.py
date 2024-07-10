from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.facke_data, name='order'),
    path('client/', views.clients_list, name='client'),
    path('client/orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('client/orders/<int:client_id>/day', views.client_orders_day, name='client_orders_day'),
    path('client/orders/<int:client_id>/mounth', views.client_orders_mounth, name='client_orders_day'),
    path('client/orders/<int:client_id>/year', views.client_orders_year, name='client_orders_day'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
    path('products/', views.get_all_products, name='products'),
      ]