# Generated by Django 4.2 on 2023-10-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats')], max_length=60),
        ),
    ]