from django import forms
from .models import Book, Movie


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title',)


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title',)



