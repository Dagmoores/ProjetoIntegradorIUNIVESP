from sys import setswitchinterval
from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.staticfiles.urls import static

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.BooksListView.as_view(), name = "list"),
    path("<slug:slug>/", views.BooksDeitalView.as_view(), name = "detail"),
]
