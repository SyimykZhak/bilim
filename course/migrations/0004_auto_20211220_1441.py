# Generated by Django 3.1.4 on 2021-12-20 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20211220_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['name'], 'verbose_name': 'курс', 'verbose_name_plural': 'курсы'},
        ),
    ]