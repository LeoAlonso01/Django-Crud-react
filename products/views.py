from .serializer import ProductSerializer
from .models import Product, Clientes, Providers, Sales, Roles, Usuarios, productsProviders
from rest_framework import viewsets

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
