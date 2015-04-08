# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchApp', '0002_auto_20150401_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=4, default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.CharField(max_length=4, default=''),
        ),
    ]
