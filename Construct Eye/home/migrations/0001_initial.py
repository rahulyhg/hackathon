# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-25 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=30)),
                ('tender_contract', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('completion_date', models.DateField()),
                ('budget', models.CharField(max_length=150)),
                ('media', models.ImageField(blank=True, upload_to='Photos')),
                ('documents', models.FileField(blank=True, upload_to='Documents')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='Report_Images')),
                ('publish', models.BooleanField(default=False)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project')),
            ],
        ),
    ]