from django.views.generic import DetailView, ListView

from .models import Books

class BooksListView(ListView):
    model = Books

class BooksDeitalView(DetailView):
    model = Books