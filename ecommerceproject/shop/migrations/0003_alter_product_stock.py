# Generated by Django 4.1.7 on 2023-02-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
