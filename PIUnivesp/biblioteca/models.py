from django.db import models
from django.db.models.fields import NullBooleanField


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique = True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    bookPhoto = models.ImageField(upload_to = "books_Img/", null = True, blank = True)
    link = models.CharField(max_length=255, default= NullBooleanField)

    def __str__(self):
        return self.title