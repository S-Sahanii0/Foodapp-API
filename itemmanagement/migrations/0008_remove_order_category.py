# Generated by Django 3.2 on 2021-04-29 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanagement', '0007_auto_20210429_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
    ]
