# Generated by Django 3.0.4 on 2020-03-11 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='is_completed',
            new_name='completed',
        ),
    ]