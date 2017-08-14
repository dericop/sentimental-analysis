# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twacount',
            fields=[
                ('acount', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('friends_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Twcoment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.CharField(max_length=140)),
                ('favourites_count', models.IntegerField()),
                ('retweet_count', models.IntegerField()),
                ('retweeted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('negative', models.FloatField()),
                ('positive', models.FloatField()),
                ('neutral', models.FloatField()),
                ('acount', models.ForeignKey(verbose_name=b'acount', to='twlogic.Twacount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
