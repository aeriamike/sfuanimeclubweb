from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class news_post(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    cover_image = models.ImageField(upload_to='img/cover/', default='img/cover/logo.jpg')
    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()
    tag = models.CharField(max_length=255, help_text="Topic of photo")


class events(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class administration(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class gallery(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    hotel_Main_Img = models.ImageField(upload_to='img/index-gallery/')
    datetime = models.DateField()
    tag = models.CharField(max_length=255, help_text="Topic of photo")


class about(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")

    body = RichTextUploadingField(blank=True, null=True)
    datetime = models.DateField()

class screenings(models.Model):

    title = models.CharField(max_length=255, help_text="Title of blog posting")
    body = RichTextUploadingField(blank=True, null=True)
    hotel_Main_Img = models.ImageField(upload_to='img/screens/')
    datetime = models.DateField()
