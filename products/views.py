from django.shortcuts import redirect, render
from .serializer import ProductSerializer, SalesSerializer, ClientesSerializer, salesCartSerializer, UsersSerializer
from .models import Product, Clientes, Providers, Sales, Roles, Usuarios, productsProviders, salesCart, cartItem
from rest_framework import viewsets
from .service import complete_sale

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class ClientesView(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer   

class salesCartView(viewsets.ModelViewSet):
    queryset = salesCart.objects.all()
    serializer_class = salesCartSerializer

class UsersView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsersSerializer
