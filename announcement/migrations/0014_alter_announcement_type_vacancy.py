# Generated by Django 3.2.9 on 2021-12-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0013_announcement_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='type_vacancy',
            field=models.CharField(choices=[('emprego', 'Emprego'), ('estagio', 'Estágio')], default='1', max_length=25),
        ),
    ]