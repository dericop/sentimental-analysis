# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0003_auto_20151103_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twcoment',
            name='favourites_count',
        ),
    ]
