# Generated by Django 4.2 on 2023-10-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]