from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Movie


class Index(TemplateView):
    template_name = 'index.html'
