# Generated by Django 3.0.5 on 2020-12-26 04:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sfuaniweb', '0012_news_post_body_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenings',
            name='colour_code',
        ),
        migrations.AddField(
            model_name='screenings',
            name='time_location',
            field=models.CharField(default=datetime.datetime(2020, 12, 26, 4, 23, 47, 245956, tzinfo=utc), help_text='When and where?', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(help_text='about', max_length=255),
        ),
        migrations.AlterField(
            model_name='administration',
            name='title',
            field=models.CharField(help_text='admin', max_length=255),
        ),
        migrations.AlterField(
            model_name='event_countdown',
            name='title',
            field=models.CharField(help_text='Name of event', max_length=255),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(help_text='event', max_length=255),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(help_text='name of photo', max_length=255),
        ),
        migrations.AlterField(
            model_name='screenings',
            name='title',
            field=models.CharField(help_text='Name of screening', max_length=255),
        ),
    ]
