# Generated by Django 4.2.3 on 2023-07-30 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_superadmin',
            new_name='is_superuser',
        ),
    ]
