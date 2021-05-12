# Generated by Django 3.2 on 2021-05-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanagement', '0012_auto_20210511_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemlist',
            name='price',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
