# Generated by Django 3.1.2 on 2020-10-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
