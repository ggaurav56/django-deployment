# Generated by Django 3.0.8 on 2020-09-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200813_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
