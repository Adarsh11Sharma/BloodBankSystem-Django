# Generated by Django 4.2 on 2023-04-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
