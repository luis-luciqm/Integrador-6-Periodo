# Generated by Django 3.2.10 on 2021-12-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0017_auto_20211211_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='type_vacancy',
            field=models.CharField(choices=[('emprego', 'Emprego'), ('estágio', 'Estágio')], default='1', max_length=25),
        ),
    ]
