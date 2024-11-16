from __future__ import annotations

from django.urls import path

from .views import loginView
from .views import logoutView
from .views import registerView

app_name = "account"
urlpatterns = [
    path("login/", loginView, name="login"),
    path("register/", registerView, name="register"),
    path("logout/", logoutView, name="logout"),
]
