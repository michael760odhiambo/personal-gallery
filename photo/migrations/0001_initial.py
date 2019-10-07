# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-06 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.CharField(max_length=30, verbose_name='Created At')),
                ('updated_at', models.CharField(max_length=30, verbose_name='Updated At')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('group', models.CharField(choices=[('land', 'Landscape'), ('sun', 'Sunset pictures'), ('moring', 'Morning Breeze'), ('tree', 'Forest'), ('ocean', 'Ocean'), ('celeb', 'Celebrity'), ('city', 'Cities')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=500)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photo.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('address', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photo.Location'),
        ),
    ]