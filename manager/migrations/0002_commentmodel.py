# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=30)),
                ('comments', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ScriptlistModel')),
            ],
        ),
    ]
