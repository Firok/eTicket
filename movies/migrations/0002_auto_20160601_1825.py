# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(max_length=1000, verbose_name='Synopsis'),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
    ]
