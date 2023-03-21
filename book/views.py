from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView , DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib import messages
from django.db.models import Q

from .models import Book, Author , Contact, BookComment
from .forms import BookCommentForm, AuthorCommentForm


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


class BookDetail(SuccessMessageMixin, DetailView):
	form = BookCommentForm
	success_message = "دیدگاه شما با موفقیت ثبت شد و پس از تایید، در سایت به نمایش گذاشته خواهد شد."


	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404 (Book.objects.actived(), slug =slug)
	
	def post(self,request, *args, **kwargs):
		form = BookCommentForm(request.POST)
		if form.is_valid():
			book = self.get_object()
			form.instance.book = book
			form.save()
			messages.success(self.request, f"دیدگاه شما با موفقیت ثبت شد و پس از تایید، در سایت به نمایش گذاشته خواهد شد.")
			return redirect (reverse('Book:book_detail' , kwargs={'slug':book.slug}))
		else:
			form = BookCommentForm()
			return render (request , 'book/form_error.html')

 
	def get_context_data(self, **kwargs):
		context =super().get_context_data(**kwargs)
		context['form'] = self.form
		return context    

 

class AuthorList(ListView):
	queryset = Author.objects.actived()
	template_name = 'book/author_list_view.html'
	context_object_name = 'authors'
	paginate_by = 6



class AuthorDetail(SuccessMessageMixin, DetailView):
	form = AuthorCommentForm
	success_message = "دیدگاه شما با موفقیت ثبت شد و پس از تایید، در سایت به نمایش گذاشته خواهد شد."

	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404 (Author.objects.actived(), slug = slug)
	
	def post(self,request, *args, **kwargs):
		form = AuthorCommentForm(request.POST)
		if form.is_valid():
			author = self.get_object()
			form.instance.author = author
			form.save()
			messages.success(self.request, f"دیدگاه شما با موفقیت ثبت شد و پس از تایید، در سایت به نمایش گذاشته خواهد شد.")

			return redirect (reverse('Book:author_detail' , kwargs={'slug':author.slug}))
		else:
			form = AuthorCommentForm()
			return render (request , 'book/form_error.html')

	def get_context_data(self, **kwargs):
		context =super().get_context_data(**kwargs)
		context['form'] = self.form
		return context    

	


class ContactUs(SuccessMessageMixin, CreateView):
	model = Contact
	fields = ['full_name', 'email', 'phone_number', 'subject', 'text']
	template_name = 'book/contact_us.html'
	success_message = "پیغام شما با موفقیت ارسال شد. همکاران ما در اسرع وقت با شما تماس خواهند گرفت."




class Search(ListView):
	template_name = 'book/search.html'
	paginate_by = 6

	def get_queryset(self):
		search = self.request.GET.get('q')
		print(search)
		return Book.objects.filter( Q(author__name__icontains = search) | Q(name__icontains = search)
		)
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')
		return context