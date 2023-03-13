from django.urls import path

from book import views

app_name = 'Book'
urlpatterns = [
    path('', views.index , name='index'),
    path('books', views.BookList.as_view() , name='book_list'),
    path('authors', views.AuthorList.as_view() , name='author_list'),
    path('book/<slug:slug>', views.BookDetail.as_view() , name='book_detail'),
    path('author/<slug:slug>', views.AuthorDetail.as_view() , name='author_detail'),
    path('contact-us', views.ContactUs.as_view() , name='contact_us'),

]






