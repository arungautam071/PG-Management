# Generated by Django 3.2.15 on 2022-09-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_management', '0006_room_management_room_user_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_management',
            name='room_floor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]