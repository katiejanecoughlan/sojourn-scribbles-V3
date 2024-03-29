# Generated by Django 4.2.11 on 2024-03-22 13:15

import cloudinary.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=django_countries.fields.CountryField(default='ZZ', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255),
        ),
    ]
