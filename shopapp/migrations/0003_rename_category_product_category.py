# Generated by Django 4.2.7 on 2023-11-06 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_rename_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
