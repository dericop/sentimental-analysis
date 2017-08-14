# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0005_auto_20151104_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twcomment',
            name='id',
        ),
        migrations.AddField(
            model_name='twcomment',
            name='Twid',
            field=models.CharField(default='none', max_length=200, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
