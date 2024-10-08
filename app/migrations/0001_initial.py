# Generated by Django 5.0.8 on 2024-08-26 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=50)),
                ('country', models.CharField(default='Unknown', max_length=50)),
                ('genre', models.CharField(default='Unknown', max_length=50)),
                ('year', models.IntegerField(default=0, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=50)),
                ('year', models.IntegerField(default=0, max_length=4)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.band')),
            ],
        ),
    ]
