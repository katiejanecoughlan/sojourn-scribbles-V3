# Generated by Django 4.2.11 on 2024-03-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='user',
        ),
    ]
