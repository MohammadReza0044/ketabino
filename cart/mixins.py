from django.shortcuts import redirect , get_object_or_404

from .models import FinalOrder


class UserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		order = get_object_or_404(FinalOrder , invoice_number = kwargs.get('invoice_number'))
		if request.user == order.user:
			return super().dispatch(request, *args, **kwargs) # type: ignore
		else:
			return redirect ('Cart:order_list')
		

