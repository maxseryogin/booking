# Generated by Django 5.1.1 on 2024-10-10 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_bookinghistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghistory',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking_app.booking'),
        ),
    ]
