# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Address', max_length=255)),
                ('street', models.CharField(verbose_name='Street name', max_length=50)),
                ('city', models.CharField(verbose_name='City', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('booking_id', models.CharField(verbose_name='Booking Id', max_length=50)),
                ('total', models.DecimalField(verbose_name='Total price', max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Cinema name', max_length=100)),
                ('description', models.CharField(verbose_name='Description', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Hall', max_length=50)),
                ('address', models.OneToOneField(verbose_name='Address', to='movies.Address')),
                ('cinema', models.ForeignKey(verbose_name='Cinema name', to='movies.Cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=100)),
                ('synopsis', models.CharField(verbose_name='Synopsis', max_length=500)),
                ('movie_type', models.CharField(verbose_name='Type', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('description', models.CharField(verbose_name='Description', max_length=500)),
                ('movie', models.ForeignKey(verbose_name='Movie', to='movies.Movie')),
                ('user', models.ForeignKey(verbose_name='MovieGoer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('row', models.CharField(verbose_name='Row', max_length=10)),
                ('no', models.IntegerField(verbose_name='Number')),
                ('seat_type', models.CharField(verbose_name='Seat type', choices=[('G', 'Gold'), ('S', 'Silver'), ('P', 'Platinum')], max_length=1)),
                ('hall', models.ForeignKey(verbose_name='Hall', to='movies.Hall')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('language', models.CharField(verbose_name='Language', max_length=50)),
                ('screen', models.CharField(verbose_name='Screen', max_length=10)),
                ('hall', models.ForeignKey(verbose_name='Hall', to='movies.Hall')),
                ('movie', models.ForeignKey(verbose_name='Movie', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('seat_type', models.CharField(verbose_name='Seat type', choices=[('G', 'Gold'), ('S', 'Silver'), ('P', 'Platinum')], max_length=1)),
                ('price', models.DecimalField(verbose_name='Price', max_digits=12, decimal_places=2)),
                ('show', models.ForeignKey(verbose_name='Show', to='movies.Show')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ManyToManyField(verbose_name='Seats', to='movies.Seat'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(verbose_name='MovieGoer', to=settings.AUTH_USER_MODEL),
        ),
    ]
