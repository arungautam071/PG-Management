# Generated by Django 3.2.15 on 2022-08-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_request', '0005_alter_washing_machine_request_take_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washing_machine_request',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
