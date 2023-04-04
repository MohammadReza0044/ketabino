from django.db import models
from django.contrib.auth.models import User

from extensions.utils import jalali_converter
from book.models import Book


class CartItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
	is_pending = models.BooleanField(default=True)
	ordered_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'Cart Item'
		ordering = ['-ordered_date']

	def __str__(self):
		return self.product.name
	


class FinalOrder(models.Model):

	STATUS_CHOICES = (
		('processing',  "در حال بررسی"),
		('sending',"در حال ارسال"),
		('ok',"ارسال شد"),
		('refund',"بازگشت از خررید"),
		)
	
	invoice_number = models.CharField(max_length=6, unique=True, blank=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
	product = models.ManyToManyField(CartItem,blank=False)
	total_payment = models.IntegerField(blank=False)
	payment_status = models.BooleanField(default=False,blank=False)
	status = models.CharField(max_length=15 , choices= STATUS_CHOICES , default='processing',blank=False)
	ordered_date = models.DateTimeField(auto_now_add=True,blank=False)


	class Meta:
		db_table = 'Final Order'
		ordering = ['-ordered_date']

	def jpublish(self):
		return jalali_converter(self.ordered_date)


