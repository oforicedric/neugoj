# Generated by Django 2.1 on 2019-12-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191215_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='potential_pics/science_student.jpeg', upload_to='profile_pics'),
        ),
    ]
