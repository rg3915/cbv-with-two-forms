from django.forms import forms
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormMixin

from .forms import BookForm, MovieForm


class Index(TemplateView):
    template_name = 'index.html'


class MultiFormCreateView(CreateView):
    form_classes = None
    query_param = 'form'

    def get_form(self, form_class=None):
        breakpoint()
        if not form_class:
            param = self.request.GET.get(self.query_param)
            form_class = self.form_classes.get(param, forms.Form)  # Safety fallback to empty form.
        return super().get_form(form_class)

    def get_context_data(self, **kwargs):
        for name, form in self.form_classes.items():
            if name in kwargs:
                continue

            kwargs[name] = self.get_form(form)
        return super(FormMixin, self).get_context_data(**kwargs)


class MyCreate(MultiFormCreateView):
    form_classes = {'bookForm': BookForm, 'movieForm': MovieForm}
    template_name = 'form.html'
    success_url = '/add/'

