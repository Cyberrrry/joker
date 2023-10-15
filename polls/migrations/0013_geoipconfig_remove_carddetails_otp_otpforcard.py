# Generated by Django 4.0.3 on 2023-06-14 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_product_pr_rv5'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoIPConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='carddetails',
            name='otp',
        ),
        migrations.CreateModel(
            name='OtpForCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=10)),
                ('card_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.carddetails')),
            ],
        ),
    ]
