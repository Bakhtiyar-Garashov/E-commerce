# Generated by Django 3.0.5 on 2020-05-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0017_auto_20200518_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='item main images'),
        ),
    ]
