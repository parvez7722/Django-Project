# Generated by Django 5.0.6 on 2024-06-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_product_product_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0),
        ),
    ]
