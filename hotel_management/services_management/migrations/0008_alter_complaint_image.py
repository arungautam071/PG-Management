# Generated by Django 3.2.15 on 2022-09-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_management', '0007_alter_complaint_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='complain_pic'),
        ),
    ]
