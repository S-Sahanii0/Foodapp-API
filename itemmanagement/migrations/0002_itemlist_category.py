# Generated by Django 3.2 on 2021-04-24 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itemmanagement.category'),
        ),
    ]
