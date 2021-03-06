# Generated by Django 2.2.6 on 2019-10-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('product_type', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('stock_count', models.PositiveIntegerField()),
                ('guarantee', models.PositiveSmallIntegerField()),
                ('shipping_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
