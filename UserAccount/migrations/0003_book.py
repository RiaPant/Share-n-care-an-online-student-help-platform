# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0002_auto_20170626_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pub_year', models.IntegerField()),
                ('pub_name', models.CharField(max_length=50)),
                ('book_cond', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], default='Old', max_length=3)),
                ('negotiable', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=3)),
                ('user_book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAccount.Profile')),
            ],
        ),
    ]