# Generated by Django 5.0.1 on 2024-05-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_panchayath_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='panchayath',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
