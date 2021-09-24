from sys import setswitchinterval
from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.staticfiles.urls import static


from . import views

app_name = "biblioteca"

urlpatterns = [
    path('', views.Home.as_view(), name = "index"),
    path('biblioteca/', views.BooksListView.as_view(), name = "list"),
    path("biblioteca/<slug:slug>/", views.BooksDeitalView.as_view(), name = "detail"), 
]