from django.urls import path
from . import views  # relative import

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about")
]
