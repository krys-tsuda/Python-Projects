# Generated by Django 4.2 on 2023-10-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
