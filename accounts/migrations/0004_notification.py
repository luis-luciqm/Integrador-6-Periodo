# Generated by Django 3.2.9 on 2021-12-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_solicitation_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solicitation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitation_notification', to='accounts.solicitation')),
            ],
        ),
    ]
