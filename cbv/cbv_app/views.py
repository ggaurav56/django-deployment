from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbv_app.models import Book
from django.urls import reverse_lazy
# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'books'
    template_name = 'cbv_app/detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'cbv_app/create.html'
    fields = ('name','isbn')
    success_url = reverse_lazy('cbv_app:list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'cbv_app/update.html'
    fields = ('name','isbn')
    success_url = reverse_lazy('cbv_app:list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'cbv_app/delete.html'
    success_url = reverse_lazy('cbv_app:list')
