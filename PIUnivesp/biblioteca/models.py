from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=255, unique = True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    bookPhoto = models.ImageField(upload_to='./dbimages/', null = True, blank = True)

    def __str__(self):
        return self.title