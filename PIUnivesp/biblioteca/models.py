from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique = True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    bookPhoto = models.ImageField(null = True, blank = True, ) #Parei aqui