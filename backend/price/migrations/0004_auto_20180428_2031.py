# Generated by Django 2.0.4 on 2018-04-28 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_price_supermarket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='price',
            name='supermarket',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='supermarkets', to='supermarket.Supermarket'),
        ),
    ]
