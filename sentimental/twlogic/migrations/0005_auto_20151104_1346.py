# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twlogic', '0004_remove_twcoment_favourites_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twcomment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=140)),
                ('retweet_count', models.IntegerField(null=True, blank=True)),
                ('retweeted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('negative', models.FloatField()),
                ('positive', models.FloatField()),
                ('neutral', models.FloatField()),
                ('query', models.CharField(max_length=140)),
                ('acount', models.ForeignKey(verbose_name=b'acount', to='twlogic.Twacount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='twcoment',
            name='acount',
        ),
        migrations.DeleteModel(
            name='Twcoment',
        ),
        migrations.AddField(
            model_name='twacount',
            name='followers_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
