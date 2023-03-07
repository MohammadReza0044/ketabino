from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Book 



def index (request):
    context = {
        "books": Book.objects.actived(),
        "new_book": Book.objects.actived()[:1]
    }
    return render (request , 'book/index.html', context)


def book_detail (request, slug):
    context = {
        "book": Book.objects.filter(slug=slug)
    }
    print(context)
    return render (request , 'book/book_detail.html', context)


def book_list_view (request):
    books = Book.objects.actived()
    paginator = Paginator(books, 6) # Show 6 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render (request , 'book/book_list_view.html', context)


  