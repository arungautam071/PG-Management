# Generated by Django 4.0 on 2022-07-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('room_type', models.CharField(max_length=50)),
                ('room_status', models.CharField(max_length=50)),
                ('check_in_date', models.DateField()),
                ('room_for', models.CharField(max_length=50)),
            ],
        ),
    ]
