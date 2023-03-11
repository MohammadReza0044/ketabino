from django.shortcuts import render , get_object_or_404 , get_list_or_404
from django.views.generic import ListView , DetailView
from django.contrib import messages

from .models import Book, Comment
from .forms import CommentForm


def index (request):
    context = {
        "books": Book.objects.actived(),
        "new_book": Book.objects.actived().latest()
    }
    return render (request , 'book/index.html', context)


class BookList(ListView):
    queryset = Book.objects.actived()
    template_name = 'book/book_list_view.html'
    context_object_name = 'books'
    paginate_by = 6


class BookDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404 (Book.objects.actived(), slug =slug)
    
