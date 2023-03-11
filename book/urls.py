from django.urls import path

from book import views

app_name = 'Book'
urlpatterns = [
    path('', views.index , name='index'),
    path('book', views.BookList.as_view() , name='book_list'),
    path('book/<slug:slug>', views.BookDetail.as_view() , name='book_detail'),

]






