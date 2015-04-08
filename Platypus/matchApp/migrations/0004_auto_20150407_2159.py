# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchApp', '0003_auto_20150407_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='number',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='dept_id',
            field=models.CharField(max_length=4, default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=64, default=''),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
