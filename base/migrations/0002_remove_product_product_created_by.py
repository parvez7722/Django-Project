# Generated by Django 5.0.6 on 2024-06-13 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_created_by',
        ),
    ]
