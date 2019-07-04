from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Book, Movie
from .forms import BookForm


class Index(TemplateView):
    template_name = 'index.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'form.html'
