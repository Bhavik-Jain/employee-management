# Generated by Django 5.0.1 on 2024-03-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_rename_role_role_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]