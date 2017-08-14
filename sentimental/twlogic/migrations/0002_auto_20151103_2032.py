# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twcoment',
            old_name='coment',
            new_name='comment',
        ),
    ]
