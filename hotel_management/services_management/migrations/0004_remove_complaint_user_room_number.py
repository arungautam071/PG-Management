# Generated by Django 4.0 on 2022-07-26 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_management', '0003_complaint_user_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='user_room_number',
        ),
    ]
