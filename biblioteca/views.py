from django.views.generic import DetailView, ListView, TemplateView

from .models import Books

class BooksListView(ListView):
    model = Books

class BooksDeitalView(DetailView):
    model = Books

class Home(TemplateView):
    template_name = './biblioteca/index.html'

class TermsOfService(TemplateView):
    template_name = './biblioteca/termsOfService.html'