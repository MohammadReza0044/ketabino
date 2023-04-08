from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from book.models import Book

from .extra import invoice_generator
from .mixins import UserAccessMixin
from .models import CartItem, FinalOrder


@login_required
def add_to_cart(request, pk):
    user = request.user
    product = Book.objects.get(pk=pk)
    new_product = CartItem.objects.create(user=user, product=product)
    messages.add_message(
        request, messages.SUCCESS, "کتاب مورد نظر به سبد خرید شما اضافه شد"
    )
    return redirect("Book:book_detail", slug=product.slug)


# geting total amount of the products
def get_total(user):
    product = CartItem.objects.filter(user=user, is_pending=True)
    total = 0
    for p in product:
        total += p.product.price
    return total


# set is_pending_false for the cart products
def is_pending_false(user):
    product = CartItem.objects.filter(user=user, is_pending=True)
    for i in product:
        i.is_pending = False
        i.save()
    return product


@login_required
def cart_view(request):
    user = request.user
    cart = CartItem.objects.filter(user=user, is_pending=True)
    cart_total = get_total(user)
    context = {"cart": cart, "cart_total": cart_total}
    return render(request, "cart/cart_preview.html", context)


@login_required
def delete(request, pk):
    user = request.user
    product = CartItem.objects.filter(user=user, pk=pk)
    product.delete()
    return redirect("Cart:cart")


@login_required
def final_order(request):
    user = request.user
    product = CartItem.objects.filter(user=user, is_pending=True)

    new_product = FinalOrder.objects.create(
        invoice_number=invoice_generator(),
        user=user,
        total_payment=get_total(user),
        payment_status=True,
    )
    new_product.product.set(product)

    product = is_pending_false(user)
    return redirect("Cart:order_detail", new_product.invoice_number)


# order list and order detail view for profile
class OrderList(LoginRequiredMixin, ListView):
    context_object_name = "order"
    template_name = "cart/order_list.html"

    def get_queryset(self):
        user = self.request.user
        return FinalOrder.objects.filter(user=user)


class OrderDetail(LoginRequiredMixin, UserAccessMixin, DetailView):
    template_name = "cart/order_detail.html"
    context_object_name = "order_detail"

    def get_object(self):
        user = self.request.user
        invoice_number = self.kwargs.get("invoice_number")
        return get_object_or_404(FinalOrder, user=user, invoice_number=invoice_number)
