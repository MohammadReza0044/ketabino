from django.shortcuts import render , get_object_or_404 , get_list_or_404
from django.views.generic import ListView , DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Book,Author , Contact
from .forms import CommentForm


def index (request):
    context = {
        "books": Book.objects.actived(),
        "new_book": Book.objects.actived().latest(),
    }
    return render (request ,'book/index.html', context)


class BookList(ListView):
    queryset = Book.objects.actived()
    template_name = 'book/book_list_view.html'
    context_object_name = 'books'
    paginate_by = 6


class BookDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404 (Book.objects.actived(), slug =slug)
    

class AuthorList(ListView):
    queryset = Author.objects.actived()
    template_name = 'book/author_list_view.html'
    context_object_name = 'authors'
    paginate_by = 6


class AuthorDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404 (Author.objects.actived(), slug = slug)
    


class ContactUs(SuccessMessageMixin,CreateView):
    model = Contact
    fields = ['full_name', 'email', 'phone_number', 'subject', 'text']
    template_name = 'book/contact_us.html'
    success_message = "پیغام شما با موفقیت ارسال شد. همکاران ما در اسرع وقت با شما تماس خواهند گرفت."

    