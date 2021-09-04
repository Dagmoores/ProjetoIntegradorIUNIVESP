from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.BooksListView.as_view(), name = "list"),
    path("<slug:slug>/", views.BooksDeitalView.as_view(), name = "detail"),
]
