# Generated by Django 5.0 on 2024-03-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinesForTyping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Character', models.CharField(max_length=25)),
                ('Line', models.TextField()),
            ],
        ),
    ]
