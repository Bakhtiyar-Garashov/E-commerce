# Generated by Django 3.0.5 on 2020-05-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0011_auto_20200517_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='item main images'),
        ),
    ]
