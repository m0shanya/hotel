# Generated by Django 4.0.1 on 2022-11-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_come',
            field=models.DateField(blank=True, help_text='2022-4-3'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_out',
            field=models.DateField(blank=True, help_text='2022-5-3'),
        ),
    ]
