# Generated by Django 3.0.5 on 2021-10-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jariyo', '0011_auto_20211015_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
