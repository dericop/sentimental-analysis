# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logicAnalisis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentsClassified',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auto_classification', models.CharField(default=b'NT', max_length=2, choices=[(b'PO', b'Positive'), (b'NE', b'Negative'), (b'NT', b'Neutral'), (b'NN', b'None')])),
                ('user_classification', models.CharField(default=b'NT', max_length=2, null=True, blank=True, choices=[(b'PO', b'Positive'), (b'NE', b'Negative'), (b'NT', b'Neutral'), (b'NN', b'None')])),
                ('text', models.TextField(default=b'')),
                ('id_page', models.CharField(max_length=200)),
                ('from_message_id', models.ForeignKey(to='logicAnalisis.message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_name', models.CharField(max_length=200, blank=True)),
                ('from_id', models.ForeignKey(to='logicAnalisis.user_facebook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='message',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='page',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='user_facebook',
            name='likes_count',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='about_me',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='age_range_end',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='age_range_init',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='birthday',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='books',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='city',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='country',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='devices',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='education',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='email',
            field=models.EmailField(max_length=70, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='friend_count',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='inspirational_people',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='locale',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='movies',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='music',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='religion',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='sex',
            field=models.CharField(default=b'M', max_length=1, null=True, blank=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='sports',
            field=models.CharField(max_length=600, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_facebook',
            name='tv',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='gram_root',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='polarity',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PO', b'Positive'), (b'NE', b'Negative'), (b'NT', b'Neutral'), (b'NN', b'None')]),
            preserve_default=True,
        ),
    ]
