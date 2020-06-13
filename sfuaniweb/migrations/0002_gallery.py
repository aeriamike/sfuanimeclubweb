# Generated by Django 3.0.5 on 2020-06-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuaniweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of blog posting', max_length=255)),
                ('hotel_Main_Img', models.ImageField(upload_to='img/index-gallery/')),
                ('datetime', models.DateField()),
            ],
        ),
    ]
