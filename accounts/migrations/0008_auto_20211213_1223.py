# Generated by Django 3.2.9 on 2021-12-13 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0017_auto_20211211_1233'),
        ('accounts', '0007_notification_participate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='participate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participate_notification', to='announcement.participateannounce'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='solicitation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitation_notification', to='accounts.solicitation'),
        ),
    ]