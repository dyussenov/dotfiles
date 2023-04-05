from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Index page of blog application")


def about(request):
    return HttpResponse("About blog application")


def categories(request, category):
    return HttpResponse(f"Посты с категорией {category}")


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def contact(request):
    return redirect("/about")