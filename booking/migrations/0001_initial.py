# Generated by Django 4.0.1 on 2022-11-27 15:45

import booking.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', validators=[booking.validators.image_resolution_check_big])),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=250)),
            ],
            options={
                'ordering': ('title',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_come', models.DateField(blank=True)),
                ('date_out', models.DateField(blank=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('count', models.IntegerField(null=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=250)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('paid', models.BooleanField(default=False)),
                ('purchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='booking.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказы')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'ordering': ('-created_at',),
            },
        ),
    ]
