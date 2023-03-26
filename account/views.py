from django.shortcuts import render , get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin 
from django.db.models import Q





