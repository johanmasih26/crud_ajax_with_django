# Generated by Django 3.1.5 on 2021-03-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20210324_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.TextField(),
        ),
    ]