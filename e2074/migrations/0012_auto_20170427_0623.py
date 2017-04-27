# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0011_auto_20170427_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='parties',
            field=models.IntegerField(default=1, verbose_name='Total Registered Parties'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='area',
            field=models.IntegerField(verbose_name='Total Area'),
        ),
        migrations.AlterField(
            model_name='country',
            name='fvoters',
            field=models.IntegerField(verbose_name='Total Female Voters'),
        ),
        migrations.AlterField(
            model_name='country',
            name='mvoters',
            field=models.IntegerField(verbose_name='Total Male Voters'),
        ),
        migrations.AlterField(
            model_name='country',
            name='officialname',
            field=models.CharField(max_length=100, verbose_name='Officaial Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.IntegerField(verbose_name='Total Population'),
        ),
        migrations.AlterField(
            model_name='country',
            name='tgvoters',
            field=models.IntegerField(verbose_name='Total Third Gender Voters'),
        ),
        migrations.AlterField(
            model_name='country',
            name='voters',
            field=models.IntegerField(verbose_name='Total Voters'),
        ),
    ]