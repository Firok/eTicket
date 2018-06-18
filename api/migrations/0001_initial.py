# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIClient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('access_token', models.CharField(blank=True, max_length=255)),
                ('expires_on', models.DateTimeField(null=True)),
                ('expired', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
            ],
        ),
    ]
