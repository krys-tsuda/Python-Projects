# Generated by Django 4.2.6 on 2023-10-09 10:40

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'University Campus',
                'verbose_name_plural': 'University Campuses',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
