# Generated by Django 2.2.3 on 2019-08-13 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190810_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]