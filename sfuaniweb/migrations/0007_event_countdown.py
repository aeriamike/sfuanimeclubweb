# Generated by Django 3.0.5 on 2020-08-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuaniweb', '0006_index_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_countdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(help_text='Title of blog posting', max_length=255)),
                ('datetime', models.DateField()),
            ],
        ),
    ]
