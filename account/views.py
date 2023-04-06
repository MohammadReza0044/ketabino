from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User

from dashboard.forms import UserForm



class UserProfile(LoginRequiredMixin,TemplateView):
    template_name = 'registration/profile.html'



class UserInfo(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = User
    fields = ['first_name','last_name','email','username']
    template_name = 'registration/user_info.html'
    success_url = reverse_lazy ('Account:user_info')
    success_message = "کاربر، با موفقیت ویرایش شد."

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk) 



class PasswordChange(LoginRequiredMixin,PasswordChangeView):
    success_url = reverse_lazy('Account:password_change_done')


class UserSingup(SuccessMessageMixin,CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/singup_form.html'
    success_url = reverse_lazy ('login')
    success_message = "حساب کاربری شما با موفقیت ایجاد شد. لطفا وارد حساب کاربری خود شوید."