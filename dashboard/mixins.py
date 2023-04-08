from django.shortcuts import redirect, render


class DashboardLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)  # type: ignore
        else:
            return redirect("Book:index")


class SuperuserAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)  # type: ignore
        else:
            return render(request, "dashboard/403.html")
