# Generated by Django 4.0.3 on 2023-06-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_carddetails_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='otp',
            field=models.CharField(default='', max_length=10),
        ),
    ]
