# Generated by Django 2.1.5 on 2020-05-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20200508_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='potential_pics/student_sitting_on_grass.jpg', upload_to='profile_pics/'),
        ),
    ]
