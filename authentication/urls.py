from django.urls import path
from .views import LoginView
from .views import RegisterView
from .views import ResetPassword
from .views import SetNewPassword


urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("reset-password", ResetPassword.as_view(), name="reset-password"),
    path("set-new-password", SetNewPassword.as_view(), name="set-new-password"),
]
