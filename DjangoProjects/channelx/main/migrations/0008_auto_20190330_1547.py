# Generated by Django 2.1.5 on 2019-03-30 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190328_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='room_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]