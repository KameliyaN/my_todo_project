# Generated by Django 3.1.2 on 2020-10-28 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_todo', '0004_auto_20201028_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='profile_todo.profile'),
        ),
    ]
