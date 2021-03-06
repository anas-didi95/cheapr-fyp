# Generated by Django 2.0.4 on 2018-04-14 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.CharField(choices=[('snack', 'Snack'), ('drink', 'Drink'), ('fresh', 'Fresh Food'), ('toilet', 'Toiletries'), ('house', 'Household'), ('ingredient', 'Ingredient')], max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('supermarket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket.Supermarket')),
            ],
        ),
    ]
