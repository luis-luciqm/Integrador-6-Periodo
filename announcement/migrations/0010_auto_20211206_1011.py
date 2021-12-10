# Generated by Django 3.2.9 on 2021-12-06 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcement', '0009_announcement_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='announces/img'),
        ),
        migrations.CreateModel(
            name='ParticipateAnnounce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.FileField(blank=True, max_length=255, upload_to='users/curriculos/')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_participate', to='announcement.announcement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_partcipate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]