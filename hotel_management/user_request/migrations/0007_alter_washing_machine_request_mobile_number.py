# Generated by Django 3.2.15 on 2022-09-01 09:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user_request', '0006_alter_washing_machine_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washing_machine_request',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]