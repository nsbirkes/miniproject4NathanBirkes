from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Quote, Category
from .forms import QuoteForm, RegisterForm


def home(request):
    defaults = ["Motivation", "Success", "Life", "Knowledge"]
    for name in defaults:
        Category.objects.get_or_create(name=name)

    latest_quotes = Quote.objects.order_by("-created_at")[:3]
    return render(request, "quotes/home.html", {"latest_quotes": latest_quotes})


def about(request):
    return render(request, "quotes/about.html")


def quote_list(request):
    quotes = Quote.objects.order_by("-created_at")
    return render(request, "quotes/quote_list.html", {"quotes": quotes})


def categories(request):
    categories = Category.objects.all()
    return render(request, "quotes/categories.html", {"categories": categories})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.created_by = request.user
            quote.save()
            return redirect("quote_list")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})