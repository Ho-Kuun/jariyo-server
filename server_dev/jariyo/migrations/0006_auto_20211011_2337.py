# Generated by Django 3.0.5 on 2021-10-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jariyo', '0005_auto_20211011_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_type',
            field=models.CharField(blank=True, choices=[('Food', '음식점'), ('Cafe', '카페')], max_length=255),
        ),
    ]
