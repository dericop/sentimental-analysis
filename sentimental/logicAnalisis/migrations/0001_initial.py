# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_likes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('id_page', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('about_me', models.CharField(max_length=200, blank=True)),
                ('categories', models.CharField(max_length=600, blank=True)),
                ('culinary_team', models.CharField(max_length=200, blank=True)),
                ('attire', models.CharField(max_length=200, blank=True)),
                ('general_manager', models.CharField(max_length=200, blank=True)),
                ('hour_init', models.CharField(max_length=20, blank=True)),
                ('hour_end', models.CharField(max_length=20, blank=True)),
                ('user_name', models.CharField(max_length=100, blank=True)),
                ('products', models.CharField(max_length=200, blank=True)),
                ('keywords', models.CharField(max_length=200, blank=True)),
                ('page_type', models.CharField(max_length=200, blank=True)),
                ('range_price', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='polarity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('per_positive', models.FloatField()),
                ('per_negative', models.FloatField()),
                ('per_neutral', models.FloatField()),
                ('classification', models.CharField(default=b'NT', max_length=2, choices=[(b'PO', b'Positive'), (b'NE', b'Negative'), (b'NT', b'Neutral')])),
                ('id_message', models.ForeignKey(to='logicAnalisis.message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user_facebook',
            fields=[
                ('id_user', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('about_me', models.CharField(max_length=200, blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('country', models.CharField(max_length=30, blank=True)),
                ('devices', models.CharField(max_length=400, blank=True)),
                ('education', models.CharField(max_length=400, blank=True)),
                ('inspirational_people', models.CharField(max_length=400, blank=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('friend_count', models.IntegerField(default=0)),
                ('age_range_init', models.IntegerField(default=0)),
                ('age_range_end', models.IntegerField(default=0)),
                ('sex', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('books', models.CharField(max_length=200, blank=True)),
                ('sports', models.CharField(max_length=600, blank=True)),
                ('music', models.CharField(max_length=200, blank=True)),
                ('locale', models.CharField(max_length=200, blank=True)),
                ('religion', models.CharField(max_length=200, blank=True)),
                ('movies', models.CharField(max_length=200, blank=True)),
                ('tv', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('polarity', models.CharField(default=b'NT', max_length=2, choices=[(b'PO', b'Positive'), (b'NE', b'Negative'), (b'NT', b'Neutral')])),
                ('gram_root', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='id_user',
            field=models.ManyToManyField(to='logicAnalisis.user_facebook'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='from_id',
            field=models.ForeignKey(to='logicAnalisis.user_facebook'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='parent_id',
            field=models.ForeignKey(to='logicAnalisis.message'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interest',
            name='id_user',
            field=models.ManyToManyField(to='logicAnalisis.user_facebook'),
            preserve_default=True,
        ),
    ]
