# Generated by Django 3.2.9 on 2021-12-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0016_auto_20211211_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='participateannounce',
            name='curriculum',
        ),
    ]
