# Generated by Django 2.1 on 2019-12-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191215_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='potential_pics/asian_student.jpeg', upload_to='profile_pics'),
        ),
    ]
