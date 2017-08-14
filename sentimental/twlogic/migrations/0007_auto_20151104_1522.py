# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0006_auto_20151104_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twcomment',
            name='created_at',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
