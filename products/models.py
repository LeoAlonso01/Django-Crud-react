from django.db import models

# Create your models here.

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    is_aviable = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Clientes(models.Model):
    id_client = models.AutoField(primary_key=True)
    document = models.CharField(max_length=10)
    type_document = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13)
    image = models.ImageField(upload_to='clientes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Providers(models.Model):
    nip = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sales(models.Model):
    id_sale = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default =0.00)
    id_client = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    id_provider = models.ForeignKey(Providers, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField( default=0)
    date = models.DateField( auto_now_add=True, null=True)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - Total: {self.total}"
    
class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Usuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE) 

    def __str__(self):
        return self.username

class productsProviders(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_product
    
class salesCart(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    id_client = models.OneToOneField(Clientes, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.cliente} con {self.quantity} de {self.id_product.name}"

class cartItem(models.Model):
    id_cartItem = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='items', null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item de {self.quantity} de {self.id_product.name} en venta {self.sales.id}"



