# Generated by Django 3.0.5 on 2020-05-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0013_auto_20200517_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='item main images/default.jpg', null=True, upload_to='item main images'),
        ),
    ]
