# Generated by Django 3.2.9 on 2021-11-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_store'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
