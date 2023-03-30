from django.urls import path
from django.contrib.auth import views


app_name = 'Account'

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done"),
#     path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
#     path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
#     path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]


from account import views

app_name = 'Account'

urlpatterns += [
    path("password-change", views.PasswordChange.as_view(), name="password_change"),
    path("profile", views.UserProfile.as_view(), name="profile"),
    path("profile/user-info", views.UserInfo.as_view(), name="user_info"),
    path("profile/sing-up", views.UserSingup.as_view(), name="singup"),

]


