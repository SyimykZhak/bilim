# Generated by Django 4.0.2 on 2022-03-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_courses_is_publicated'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='task',
            field=models.FileField(null=True, upload_to='', verbose_name='задание к уроку'),
        ),
    ]
