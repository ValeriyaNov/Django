from django.contrib import admin
from .import models


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)


@admin.register(models.Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['-quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    
    readonly_fields = ['added_date']
    fieldsets = [
        (
            None, {  
                'classes': ['wide'],  
                'fields': ['name'],  
            },
        ),
        (
            'Подробности',  
            {
                'classes': ['collapse'],  
                'description': 'Категория товара и его подробное описание',  
                'fields': ['category', 'description'],  
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'

    readonly_fields = ['registration_date']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount']

    readonly_fields = ['order_date']
