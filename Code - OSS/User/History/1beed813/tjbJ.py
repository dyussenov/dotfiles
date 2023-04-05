from datetime import date

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.utils.text import slugify
from .forms import *
from .models import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class QuestionsHome(ListView):
    model = Question
    template_name = 'questions_home.html'
    context_object_name = 'questions'

    def get_queryset(self):
        questions = Question.objects.all()
        if self.kwargs.get('category_slug'):
            return questions.filter(category__slug=self.kwargs['category_slug'])
        return questions


def show_question(request, question_slug):
    return render(request, 'question.html')

@login_required
def add_question(request):
    if request.method == 'POST':
        #user = get_user_model()
        form = AddQuestionForm(request.POST)
        new_question = Question(
            author=CustomUser(pk=request.user.id),
            title=form.data['title'],
            slug=slugify(form.data['title']),
            body=form.data['body'],
            category=Category.objects.get(pk=form.data['category'][0])
        )
        new_question.save()
        print(form.data, request.user.id)
        return redirect('home')
    else:
        form = AddQuestionForm()
        return render(request, "add_question.html", {'form': form})


def index(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("About blog application")


def category_questions(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    questions = Question.objects.filter(category=category)
    context = {
        'cat_selected': category,
        'questions': questions
    }
    return render(request, "questions.html", context)


def contact(request):
    return redirect("/about")


def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

'''
def archive(request, year):
    if int(year) > date.today().year or int(year) < 2015:
        raise Http404()
 
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")'''