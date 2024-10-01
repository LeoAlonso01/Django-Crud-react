from rest_framework import serializers
from .models import Product, Clientes, Providers, Sales, Roles, Usuarios, productsProviders

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    