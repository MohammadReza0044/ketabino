from django.urls import path
from account import views


app_name = 'Account'

urlpatterns = [
    path("profile", views.UserProfile.as_view(), name="profile"),
    path("profile/user-info", views.UserInfo.as_view(), name="user_info"),
    path("profile/sing-up", views.UserSingup.as_view(), name="singup"),

]


