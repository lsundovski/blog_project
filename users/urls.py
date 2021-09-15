from django.urls import path
from . import views  # relative import


urlpatterns = [
    path("register/", views.register, name="users-register"),
]
