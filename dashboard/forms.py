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
			user.is_active = True
			user.save()
		return user


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'is_superuser','is_staff','is_active']

	def save(self, commit=True):
		user = super(UserUpdateForm, self).save(commit=False)
		if commit:
			user.save()
		return user


class UserProfileForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		user = kwargs.pop('user')
		super(UserProfileForm,self).__init__(*args,**kwargs)
		if not user.is_superuser:
			self.fields['username'].disabled=True
			self.fields['is_superuser'].disabled=True
			self.fields['is_staff'].disabled=True
			self.fields['is_active'].disabled=True

	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'is_superuser','is_staff','is_active']

	def save(self, commit=True):
		user = super(UserProfileForm, self).save(commit=False)
		if commit:
			user.save()
		return user
