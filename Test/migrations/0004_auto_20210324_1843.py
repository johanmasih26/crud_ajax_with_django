# Generated by Django 3.1.5 on 2021-03-24 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0003_auto_20210324_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hello',
            name='date',
        ),
        migrations.RemoveField(
            model_name='hello',
            name='desc',
        ),
    ]