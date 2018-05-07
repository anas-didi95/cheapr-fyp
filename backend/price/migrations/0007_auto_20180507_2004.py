# Generated by Django 2.0.5 on 2018-05-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0006_auto_20180503_0741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['-year_start', '-month_start', '-day_start', '-description']},
        ),
        migrations.AlterField(
            model_name='price',
            name='supermarket',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='supermarket.Supermarket'),
        ),
    ]
