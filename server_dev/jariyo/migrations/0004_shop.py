# Generated by Django 3.0.5 on 2021-10-11 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jariyo', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_photo', models.ImageField(blank=True, upload_to='')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('shop_type', models.CharField(max_length=20)),
                ('sit_over4_max', models.IntegerField(max_length=4)),
                ('sit_4_max', models.IntegerField(max_length=4)),
                ('sit_2_max', models.IntegerField(max_length=4)),
                ('sit_over4', models.IntegerField(max_length=4)),
                ('sit_4', models.IntegerField(max_length=4)),
                ('sit_2', models.IntegerField(max_length=4)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
