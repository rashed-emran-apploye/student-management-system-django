# Generated by Django 3.1.1 on 2021-05-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='static/dist/img/avatar2.png', upload_to=''),
        ),
    ]
