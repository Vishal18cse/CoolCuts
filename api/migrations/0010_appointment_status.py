# Generated by Django 5.0.6 on 2024-07-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_appointment_user_alter_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=10),
        ),
    ]
