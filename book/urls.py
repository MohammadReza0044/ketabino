from django.urls import path

from book import views

app_name = 'Book'
urlpatterns = [
    path('', views.index , name='index'),
    path('book', views.book_list_view , name='book_list'),
    path('book/<slug:slug>', views.book_detail , name='book_detail'),

]






