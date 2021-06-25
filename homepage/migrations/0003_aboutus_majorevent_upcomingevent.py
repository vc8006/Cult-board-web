# Generated by Django 3.2.4 on 2021-06-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_rename_welcomenote_welcomenote_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CMsays', models.CharField(max_length=1000)),
                ('GSsays', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='majorevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='default.jpg', upload_to='media/team')),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='upcomingevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='default.jpg', upload_to='media/team')),
                ('host_date', models.DateTimeField()),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
