# Generated by Django 5.0.1 on 2024-03-03 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='name',
        ),
    ]
