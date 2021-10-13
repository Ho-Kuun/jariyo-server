# Generated by Django 3.0.5 on 2021-10-11 14:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('jariyo', '0006_auto_20211011_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_type',
            field=models.CharField(blank=True, choices=[('R', 'Restaurant'), ('C', 'Cafe')], max_length=1),
        ),
    ]