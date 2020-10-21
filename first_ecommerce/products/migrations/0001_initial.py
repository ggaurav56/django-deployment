# Generated by Django 3.0.8 on 2020-08-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=156)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'ordering': ('-posted_at',),
            },
        ),
    ]
