# Generated by Django 2.0.4 on 2018-05-03 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_auto_20180428_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['-year_start', '-month_start', '-day_start']},
        ),
    ]