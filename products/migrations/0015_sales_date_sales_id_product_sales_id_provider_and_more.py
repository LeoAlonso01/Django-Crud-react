# Generated by Django 4.2.16 on 2024-10-02 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_clientes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='id_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='sales',
            name='id_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.providers'),
        ),
        migrations.AddField(
            model_name='sales',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total',
            field=models.FloatField(),
        ),
    ]
