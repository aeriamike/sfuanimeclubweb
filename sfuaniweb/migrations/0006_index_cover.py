# Generated by Django 3.0.5 on 2020-08-28 05:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuaniweb', '0005_auto_20200827_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of cover image', max_length=255)),
                ('cover_image', models.ImageField(default='img/cover/logo.jpg', upload_to='img/cover/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('link', models.CharField(help_text='Id number that links to the webpage', max_length=255)),
            ],
        ),
    ]
