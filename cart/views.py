from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

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


@login_required
def cart_view(request):
	user=request.user
	cart = CartItem.objects.filter(user=user , is_pending = True)
	cart_total = 0
	
	for p in cart:
		cart_total += p.product.price
	
	context = {
		'cart': cart,
		'cart_total':cart_total
	}
	return render (request, 'cart/cart_preview.html',context)



@login_required
def delete(request,pk):
	user = request.user
	product = CartItem.objects.filter(user=user , pk=pk)
	product.delete()
	return redirect ('Cart:cart')



def cart_item_sum(request):
	user = request.user
	product = CartItem.objects.filter(user=user, is_pending = True)
	print(product)
	return render