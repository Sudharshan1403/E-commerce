# Generated by Django 4.2.2 on 2023-07-11 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nammashop', '0005_remove_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]