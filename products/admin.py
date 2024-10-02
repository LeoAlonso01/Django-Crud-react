from django.contrib import admin
from .models import Product, Clientes, Providers, Sales, Roles, Usuarios, productsProviders, salesCart

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id_product','name', 'price', 'stock', 'is_aviable', 'created_at','updated_at']
    list_filter = ['is_aviable', 'created_at', 'updated_at']
    search_fields = ['name', 'price']
    list_editable = ['price', 'stock', 'is_aviable']
    date_hierarchy = 'created_at'
    list_per_page = 10

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['id_client','document', 'type_document', 'name', 'last_name', 'email', 'phone', 'rfc', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    list_per_page = 10

@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ['nip','name', 'city', 'email', 'phone', 'rfc', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    list_per_page = 10

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['id_sale','id_client', 'id_product', 'id_provider', 'quantity', 'date', 'total', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['id_sale']
    list_per_page = 10


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['id_role']
    list_per_page = 10


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id_user','username', 'password', 'email','created_at', 'role']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    list_per_page = 10



# This code registers the Product model with the admin site. The admin.site.register() method is a decorator that takes a model class as an argument and returns a class that is registered with the admin site. The ProductAdmin class is a subclass of ModelAdmin, which is a class that defines the behavior of the admin interface for a model. The ProductAdmin class defines the
# list_display attribute, which is a list of field names that will be displayed in the admin interface. The list_filter attribute is a list of field names that will be used to filter the list of products in the admin interface. The search_fields attribute is a list of field names that will be used to search for products in the admin interface. The list_editable attribute is a list of field names that can be edited directly in the list of products in the admin interface. The date_hierarchy attribute is the name of the field that will be used to filter the list of products by date. The list_per_page attribute is the number of products that will be displayed per page in the admin interface.
# 
# The admin.site.register() method is a decorator that takes a model class as an argument and returns a class that is registered with the admin site. The ProductAdmin class is a subclass of ModelAdmin, which is a class that defines the behavior of the admin interface for a model. The ProductAdmin class defines the
# list_display attribute, which is a list of field names that will be displayed in the admin interface. The list_filter attribute is a list of field names that will be used to filter the list of products in the admin interface. The search_fields attribute is a list of field names that will be used to search for products in the admin interface. The list_editable attribute is a list of field names that can be edited directly in the list of products in the admin interface. The date_hierarchy attribute is the name of the field that will be used to filter the list of products by date. The list_per_page attribute is the number of products that will be displayed per page in the admin interface.

