# Generated by Django 4.0.2 on 2022-03-08 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_ratingstar_alter_teachers_options_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
