from django.contrib import admin

# Register your models here.

from .models import Books

@admin.register(Books)

class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "bookPhoto")