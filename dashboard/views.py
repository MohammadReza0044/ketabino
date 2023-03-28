from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin 
from django.db.models import Q

from django.contrib.auth.models import User

from .forms import UserForm , UserUpdateForm
from book.models import Book , Author, Publisher, Translator, BookComment, AuthorComment



class DashboardIndex(LoginRequiredMixin, ListView):
    queryset = Book.objects.actived()
    template_name = 'dashboard/index.html'

# book classes
class BookDashboard(LoginRequiredMixin , ListView):
    queryset = Book.objects.all()
    template_name = 'dashboard/book_list.html'
    paginate_by = 10



class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'dashboard/book_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:book_list')


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'dashboard/book_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:book_list')


# author classes
class AuthorDashboard(LoginRequiredMixin , ListView):
    queryset = Author.objects.all()
    template_name = 'dashboard/author_list.html'
    paginate_by = 10



class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'dashboard/author_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:author_list')


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'dashboard/author_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:author_list')


# publisher classes
class PublisherDashboard(LoginRequiredMixin , ListView):
    queryset = Publisher.objects.all()
    template_name = 'dashboard/publisher_list.html'
    paginate_by = 10



class PublisherCreate(LoginRequiredMixin, CreateView):
    model = Publisher
    template_name = 'dashboard/publisher_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:publisher_list')


class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = Publisher
    template_name = 'dashboard/publisher_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:publisher_list')


# translator classes
class TranslatorDashboard(LoginRequiredMixin , ListView):
    queryset = Translator.objects.all()
    template_name = 'dashboard/translator_list.html'
    paginate_by = 10


class TranslatorCreate(LoginRequiredMixin, CreateView):
    model = Translator
    template_name = 'dashboard/translator_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:translator_list')


class TranslatorUpdate(LoginRequiredMixin, UpdateView):
    model = Translator
    template_name = 'dashboard/translator_create_update.html'
    fields = '__all__'
    success_url = reverse_lazy ('Dashboard:translator_list')


# comment classes
class BookCommentDashboard(LoginRequiredMixin , ListView):
    queryset = BookComment.objects.all()
    template_name = 'dashboard/book_comment_list.html'
    paginate_by = 10



class AuthorCommentDashboard(LoginRequiredMixin , ListView):
    queryset = AuthorComment.objects.all()
    template_name = 'dashboard/author_comment_list.html'
    paginate_by = 10



class BookCommentDetail(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/book_comment_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404 (BookComment , pk=pk)
    

class AuthorCommentDetail(LoginRequiredMixin, DeleteView):
    template_name = 'dashboard/author_comment_detail.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404 (AuthorComment , pk=pk)
    

class BookCommentDelete(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = BookComment
    template_name = 'dashboard/delete_confirm.html'
    success_url = reverse_lazy ('Dashboard:book-comments_list')
    success_message = "دیدگاه، با موفقیت حذف شد."


class AuthorCommentDelete(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = AuthorComment
    template_name = 'dashboard/delete_confirm.html'
    success_url = reverse_lazy ('Dashboard:author-comments_list')
    success_message = "دیدگاه، با موفقیت حذف شد."


class BookCommentActive(LoginRequiredMixin, UpdateView):
    fields = ('active','is_read')
    template_name = 'dashboard/comment_active.html'
    success_url = reverse_lazy ('Dashboard:book-comments_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return BookComment.objects.get(pk=pk)


class AuthorCommentActive(LoginRequiredMixin, UpdateView):
    fields = ('active','is_read')
    template_name = 'dashboard/comment_active.html'
    success_url = reverse_lazy ('Dashboard:author-comments_list')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return AuthorComment.objects.get(pk=pk)
    

# publisher classes
class UserDashboard(LoginRequiredMixin , ListView):
    queryset = User.objects.all().order_by('-is_superuser','-is_staff')
    template_name = 'dashboard/user_list.html'
    paginate_by = 10


class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'dashboard/user_create_update.html'
    success_url = reverse_lazy ('Dashboard:user_list')\


class UserUpdate(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'dashboard/user_create_update.html'
    success_url = reverse_lazy ('Dashboard:user_list')
    success_message = "کاربر، با موفقیت ویراش شد."

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404 (User , pk=pk)


class UserDelete(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'dashboard/delete_confirm.html'
    success_url = reverse_lazy ('Dashboard:user_list')
    success_message = "دیدگاه، با موفقیت حذف شد."