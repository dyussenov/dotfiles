from datetime import date

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, AddQuestionForm

u = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def add_question(request):
    print(u.id)
    if request.method == 'POST':
        form =  AddQuestionForm(request.POST)
        if form.is_valid():
            print(request)
            #form.save()
            return redirect('home')

    else:
        form = AddQuestionForm()
        return render(request, "add_question.html", {'form': form, 'u': u})


def index(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("About blog application")


def categories(request, category):
    return HttpResponse(f"Посты с категорией {category}")


def contact(request):
    return redirect("/about")


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def archive(request, year):
    if(int(year) > date.today().year or int(year) < 2015):
        raise Http404()
 
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")