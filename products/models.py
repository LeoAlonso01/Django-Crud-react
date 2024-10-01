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
    id_client = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.quantity} de {self.id_product} a {self.id_client}"
    
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.id_product.price
        self.id_product.stock -= self.quantity
        super(Sales, self).save(*args, **kwargs)
        if self.id_product.stock < 0:
            raise ValueError('No hay suficiente stock')
        self.id_product.save()
        super(Sales, self).save(*args, **kwargs)
        
    
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
    

