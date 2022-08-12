# Generated by Django 3.2.15 on 2022-08-05 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Amenities_Request_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_type_request', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=100)),
                ('service_status', models.CharField(max_length=50)),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
