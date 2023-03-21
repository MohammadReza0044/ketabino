from django.urls import path
from django.contrib.auth import views


app_name = 'Account'

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
#     path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
#     path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done"),
#     path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
#     path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
#     path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]


from account import views

urlpatterns += [
    path('admin-dashboard', views.DashboardIndex.as_view() , name='dashboard'),
    path('admin-dashboard/books', views.BookDashboard.as_view() , name='book_list'),
    path('admin-dashboard/book-create', views.BookCreate.as_view() , name='book_create'),
    path('admin-dashboard/book-update/<int:pk>', views.BookUpdate.as_view() , name='book_update'),
    path('admin-dashboard/authors', views.AuthorDashboard.as_view() , name='author_list'),
    path('admin-dashboard/author-create', views.AuthorCreate.as_view() , name='author_create'),
    path('admin-dashboard/author-update/<int:pk>', views.AuthorUpdate.as_view() , name='author_update'),
    path('admin-dashboard/publishers', views.PublisherDashboard.as_view() , name='publisher_list'),
    path('admin-dashboard/publisher-create', views.PublisherCreate.as_view() , name='publisher_create'),
    path('admin-dashboard/publisher-update/<int:pk>', views.PublisherUpdate.as_view() , name='publisher_update'),
    path('admin-dashboard/translators', views.TranslatorDashboard.as_view() , name='translator_list'),
    path('admin-dashboard/translator-create', views.TranslatorCreate.as_view() , name='translator_create'),
    path('admin-dashboard/translator-update/<int:pk>', views.TranslatorUpdate.as_view() , name='translator_update'),
    path('admin-dashboard/book-comments', views.BookCommentDashboard.as_view() , name='book-comments_list'),
    path('admin-dashboard/author-comments', views.AuthorCommentDashboard.as_view() , name='author-comments_list'),



]






