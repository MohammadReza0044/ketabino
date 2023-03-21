from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.db.models import Q

from book.models import Book , Author, Publisher, Translator, BookComment, AuthorComment


class DashboardIndex(LoginRequiredMixin, ListView):
    queryset = Book.objects.actived()
    template_name = 'registration/index.html'


class BookDashboard(LoginRequiredMixin , ListView):
    queryset = Book.objects.all()
    template_name = 'registration/book_list.html'
    paginate_by = 10



class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'registration/book_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:book_list')


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'registration/book_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:book_list')



class AuthorDashboard(LoginRequiredMixin , ListView):
    queryset = Author.objects.all()
    template_name = 'registration/author_list.html'
    paginate_by = 10



class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'registration/author_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:author_list')


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'registration/author_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:author_list')



class PublisherDashboard(LoginRequiredMixin , ListView):
    queryset = Publisher.objects.all()
    template_name = 'registration/publisher_list.html'
    paginate_by = 10



class PublisherCreate(LoginRequiredMixin, CreateView):
    model = Publisher
    template_name = 'registration/publisher_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:publisher_list')


class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = Publisher
    template_name = 'registration/publisher_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:publisher_list')



class TranslatorDashboard(LoginRequiredMixin , ListView):
    queryset = Translator.objects.all()
    template_name = 'registration/translator_list.html'
    paginate_by = 10


class TranslatorCreate(LoginRequiredMixin, CreateView):
    model = Translator
    template_name = 'registration/translator_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:translator_list')


class TranslatorUpdate(LoginRequiredMixin, UpdateView):
    model = Translator
    template_name = 'registration/translator_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Account:translator_list')



class BookCommentDashboard(LoginRequiredMixin , ListView):
    queryset = BookComment.objects.all()
    template_name = 'registration/book_comment_list.html'
    paginate_by = 10



class AuthorCommentDashboard(LoginRequiredMixin , ListView):
    queryset = AuthorComment.objects.all()
    template_name = 'registration/author_comment_list.html'
    paginate_by = 10
