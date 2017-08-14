# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0002_auto_20151103_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='twcoment',
            name='query',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='twacount',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twacount',
            name='friends_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twacount',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twcoment',
            name='retweet_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
