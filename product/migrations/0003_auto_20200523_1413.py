# Generated by Django 3.0.6 on 2020-05-23 20:13

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
