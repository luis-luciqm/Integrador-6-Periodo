# Generated by Django 3.2.9 on 2021-12-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0010_auto_20211206_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participateannounce',
            name='curriculum',
            field=models.FileField(max_length=255, upload_to='users/curriculos/'),
        ),
    ]
