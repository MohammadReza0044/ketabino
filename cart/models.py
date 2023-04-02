from django.db import models
from django.contrib.auth.models import User

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
	
