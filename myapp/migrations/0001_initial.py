# Generated by Django 5.1.3 on 2024-12-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('highest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lowest_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
