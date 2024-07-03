from django.urls import path
from . import views
urlpatterns = [
    
    path('order/', views.facke_data, name='order'),
      ]