# Generated by Django 3.2.9 on 2021-12-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='curriculum',
            field=models.FileField(null=True, upload_to='users/curriculos/'),
        ),
    ]