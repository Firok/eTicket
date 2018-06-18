# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20160601_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Genre', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Media', max_length=50)),
                ('image', models.ImageField(verbose_name='Image', upload_to='movies/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('trailer', models.FileField(verbose_name='Trailer', upload_to='movies/trailers/')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_type',
        ),
        migrations.AddField(
            model_name='movie',
            name='origin',
            field=models.CharField(default='INDIA', verbose_name='Origin', max_length=50),
        ),
        migrations.AlterField(
            model_name='show',
            name='screen',
            field=models.CharField(verbose_name='Format', max_length=10),
        ),
        migrations.AddField(
            model_name='trailer',
            name='movie',
            field=models.OneToOneField(to='movies.Movie', verbose_name='Movie'),
        ),
        migrations.AddField(
            model_name='media',
            name='movie',
            field=models.ForeignKey(verbose_name='Movie', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.Genre', verbose_name='Genre'),
        ),
    ]
