from django.urls import path

from account import views

app_name = 'Account'
urlpatterns = [
    path('', views.index , name='index'),


]






