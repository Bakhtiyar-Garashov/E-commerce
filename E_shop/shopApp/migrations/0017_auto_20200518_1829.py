# Generated by Django 3.0.5 on 2020-05-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0016_auto_20200517_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='item main images'),
        ),
    ]
