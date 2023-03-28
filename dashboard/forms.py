from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name','last_name', 'email', 'is_superuser','is_staff','is_active']
		widgets = {
			'password': forms.PasswordInput()
		}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name','last_name', 'email', 'is_superuser','is_staff','is_active']

	def save(self, commit=True):
		user = super(UserUpdateForm, self).save(commit=False)
		password = self.cleaned_data["password"]
		if password:
			user.set_password(password)
			if commit:
				user.save()
		return user