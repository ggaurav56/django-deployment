# Generated by Django 3.0.8 on 2020-09-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200905_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default='', max_length=156, unique=True),
        ),
    ]
