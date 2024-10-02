from rest_framework import serializers
from .models import Product, Clientes, Providers, Sales, Roles, Usuarios, productsProviders, salesCart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class salesCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = salesCart
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'