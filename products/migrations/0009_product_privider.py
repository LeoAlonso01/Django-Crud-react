# Generated by Django 4.2.16 on 2024-10-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_providers_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='privider',
            field=models.ManyToManyField(blank=True, related_name='products', through='products.productsProviders', to='products.providers'),
        ),
    ]
