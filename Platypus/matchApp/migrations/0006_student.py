# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchApp', '0005_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('student_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(default='', max_length=64)),
                ('last_name', models.CharField(default='', max_length=64)),
                ('user_id', models.CharField(default='', max_length=64)),
                ('password', models.CharField(default='', max_length=64)),
                ('email_address', models.CharField(default='', max_length=128)),
                ('course_list', models.CharField(default='', max_length=1024)),
            ],
        ),
    ]
