# Generated by Django 3.2.6 on 2021-08-13 03:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]