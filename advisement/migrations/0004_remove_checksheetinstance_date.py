# Generated by Django 3.1.5 on 2021-01-22 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisement', '0003_auto_20210122_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checksheetinstance',
            name='date',
        ),
    ]
