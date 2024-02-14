from django.shortcuts import render
from django.views import View


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "authentication/register.html")


class ResetPassword(View):
    def get(self, request):
        return render(request, "authentication/reset-password.html")


class SetNewPassword(View):
    def get(self, request):
        return render(request, "authentication/set-new-password.html")
