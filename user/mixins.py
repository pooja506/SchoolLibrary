from django.contrib.auth.mixins import AccessMixin,LoginRequiredMixin, PermissionDenied
from django.urls import reverse_lazy


class LoginRequired404Mixin(LoginRequiredMixin):
    login_url = reverse_lazy('account:login')

class SuperuserRequiredMixin(LoginRequiredMixin):
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)