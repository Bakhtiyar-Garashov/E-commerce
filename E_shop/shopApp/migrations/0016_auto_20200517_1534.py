# Generated by Django 3.0.5 on 2020-05-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0015_auto_20200517_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='item main images'),
        ),
    ]