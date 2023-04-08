from django.urls import path

from dashboard import views

app_name = "Dashboard"
urlpatterns = [
    path("", views.DashboardIndex.as_view(), name="dashboard"),
    path("orders", views.OrderDashboard.as_view(), name="order_list"),
    path("order/<int:pk>", views.OrderDetail.as_view(), name="order_detail"),
    path("order-update/<int:pk>", views.OrderUpdate.as_view(), name="order_update"),
    path("books", views.BookDashboard.as_view(), name="book_list"),
    path("book-create", views.BookCreate.as_view(), name="book_create"),
    path("book-update/<int:pk>", views.BookUpdate.as_view(), name="book_update"),
    path("authors", views.AuthorDashboard.as_view(), name="author_list"),
    path("author-create", views.AuthorCreate.as_view(), name="author_create"),
    path("author-update/<int:pk>", views.AuthorUpdate.as_view(), name="author_update"),
    path("publishers", views.PublisherDashboard.as_view(), name="publisher_list"),
    path("publisher-create", views.PublisherCreate.as_view(), name="publisher_create"),
    path(
        "publisher-update/<int:pk>",
        views.PublisherUpdate.as_view(),
        name="publisher_update",
    ),
    path("translators", views.TranslatorDashboard.as_view(), name="translator_list"),
    path(
        "translator-create", views.TranslatorCreate.as_view(), name="translator_create"
    ),
    path(
        "translator-update/<int:pk>",
        views.TranslatorUpdate.as_view(),
        name="translator_update",
    ),
    path(
        "book-comments", views.BookCommentDashboard.as_view(), name="book-comments_list"
    ),
    path(
        "author-comments",
        views.AuthorCommentDashboard.as_view(),
        name="author-comments_list",
    ),
    path(
        "book-comment/<int:pk>",
        views.BookCommentDetail.as_view(),
        name="book_comment_detail",
    ),
    path(
        "author-comment/<int:pk>",
        views.AuthorCommentDetail.as_view(),
        name="author_comment_detail",
    ),
    path(
        "book-comment_delete/<int:pk>",
        views.BookCommentDelete.as_view(),
        name="book_comment_delete",
    ),
    path(
        "author-comment_delete/<int:pk>",
        views.AuthorCommentDelete.as_view(),
        name="author_comment_delete",
    ),
    path(
        "book-comment_active/<int:pk>",
        views.BookCommentActive.as_view(),
        name="book_comment_active",
    ),
    path(
        "author-comment_active/<int:pk>",
        views.AuthorCommentActive.as_view(),
        name="author_comment_active",
    ),
    path("contact-us", views.ContactUsDashboard.as_view(), name="contact_us_list"),
    path(
        "contactus/<int:pk>", views.ContactUsDetail.as_view(), name="contact_us_detail"
    ),
    path(
        "contact-us_active/<int:pk>",
        views.ContactUsActive.as_view(),
        name="contact_us_active",
    ),
    path(
        "contact-us-delete/<int:pk>",
        views.ContactUsDelete.as_view(),
        name="contact_us_delete",
    ),
    path("users", views.UserDashboard.as_view(), name="user_list"),
    path("user-create", views.UserCreate.as_view(), name="user_create"),
    path("user-update/<int:pk>", views.UserUpdate.as_view(), name="user_update"),
    path("user-delete/<int:pk>", views.UserDelete.as_view(), name="user_delete"),
    path("user-profile", views.UserProfile.as_view(), name="user_profile"),
]


from django.contrib.auth import views

urlpatterns += [path("logout", views.LogoutView.as_view(), name="logout")]
