from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("quotes/", views.quote_list, name="quote_list"),
    path("categories/", views.categories, name="categories"),
    path("add/", views.add_quote, name="add_quote"),
    path("register/", views.register, name="register"),
]