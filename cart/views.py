from django.shortcuts import render , redirect , get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from book.models import Book
from .models import CartItem

@login_required
def add_to_cart(request,pk):
	user = request.user
	product = Book.objects.get(pk=pk)
	print(product)
	new_product = CartItem.objects.create(
		user = user,
		product = product
	)
	messages.add_message(request, messages.SUCCESS, 'کتاب مورد نظر به سبد خرید شما اضافه شد')
	return redirect ('Book:book_detail' , slug = product.slug)


class CartItemList(LoginRequiredMixin,ListView):
	model = CartItem
	context_object_name = 'cart'
	template_name = 'cart/cart_preview.html'
	

	def get_queryset(self):
		queryset = super(CartItemList, self).get_queryset()
		queryset = queryset.filter(user=self.request.user , is_pending = True )
		return queryset