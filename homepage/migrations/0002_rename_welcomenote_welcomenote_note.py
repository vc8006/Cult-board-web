# Generated by Django 3.2.4 on 2021-06-25 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='welcomenote',
            old_name='welcomenote',
            new_name='note',
        ),
    ]