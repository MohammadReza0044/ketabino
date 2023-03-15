from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView , DetailView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Book, Author , Contact, BookComment
from .forms import BookCommentForm


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
    form = BookCommentForm

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404 (Book.objects.actived(), slug =slug)
    
    def post(self,request, *args, **kwargs):
        form = BookCommentForm(request.POST)
        if form.is_valid():
            book = self.get_object()
            form.instance.book = book
            form.save()
            return redirect (reverse('Book:book_detail' , kwargs={'slug':book.slug}))
        else:
            form = BookCommentForm()
            return render (request , 'book/form_error.html')

 
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['form'] = self.form
        return context    

 
class CreateArticleComment(CreateView):
    model = BookComment 
    fields = ('name' , 'email' ,'text')

    def post_valid(self, form):
        book = get_object_or_404(Book, slug=self.kwargs['slug'])
        articlecomment = form.save(commit=False)
        articlecomment.article = book
        articlecomment.save()
        return redirect('Book:book_detail', slug=book.slug)

    def get_success_url(self):
        return reverse_lazy('Book:book_detail')


class AuthorList(ListView):
    queryset = Author.objects.actived()
    template_name = 'book/author_list_view.html'
    context_object_name = 'authors'
    paginate_by = 6


class AuthorDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404 (Author.objects.actived(), slug = slug)
    


class ContactUs(SuccessMessageMixin, CreateView):
    model = Contact
    fields = ['full_name', 'email', 'phone_number', 'subject', 'text']
    template_name = 'book/contact_us.html'
    success_message = "پیغام شما با موفقیت ارسال شد. همکاران ما در اسرع وقت با شما تماس خواهند گرفت."


