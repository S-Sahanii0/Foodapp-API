# Generated by Django 3.2 on 2021-04-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanagement', '0003_auto_20210429_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='c_image',
        ),
    ]
