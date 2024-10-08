# Generated by Django 4.2.16 on 2024-10-02 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_salescart'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescart',
            name='id_client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.clientes'),
        ),
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id_cartItem', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('salesCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.salescart')),
            ],
        ),
    ]
