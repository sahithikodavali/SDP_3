# Generated by Django 5.0 on 2024-03-09 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_user_delete_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]