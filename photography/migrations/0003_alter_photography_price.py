# Generated by Django 4.1.3 on 2022-12-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0002_rename_foodchoice_photography_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
