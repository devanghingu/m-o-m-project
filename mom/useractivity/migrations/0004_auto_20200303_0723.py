# Generated by Django 3.0.3 on 2020-03-03 07:23

from django.db import migrations, models
import useractivity.models


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0003_auto_20200228_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='profileimage/user_default.jpg', upload_to=useractivity.models.user_directory_path),
        ),
    ]
