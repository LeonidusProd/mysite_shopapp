# Generated by Django 4.2 on 2023-12-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
