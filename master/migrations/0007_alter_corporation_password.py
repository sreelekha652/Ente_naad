# Generated by Django 5.0.1 on 2024-05-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_corporation_muncipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporation',
            name='password',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
