from django.http import HttpResponse

class DashboardLoginMixin():

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser or request.user.is_staff:
			return super().dispatch(request, *args, **kwargs) # type: ignore
		else:
			return HttpResponse ('شما اجازه ی ورود ندارید')
		

