from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model
#from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.utils.text import slugify

from .forms import *
from .models import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AddQuestionView(CreateView):
    form_class = AddQuestionForm
    template_name = 'add_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.data['title'])
        return super(AddQuestionView, self).form_valid(form)


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions_home.html'
    context_object_name = 'questions'
    paginate_by = 10

    def get_queryset(self):
        questions = Question.objects.all()
        if self.kwargs.get('category_slug'):
            return questions.filter(category__slug=self.kwargs['category_slug'])
        return questions


    '''def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', '')
        return context'''


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'
    slug_url_kwarg = 'question_slug'
    context_object_name = 'question'


def index(request):
    return render(request, "home.html")


'''def category_questions(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    questions = Question.objects.filter(category=category)
    context = {
        'cat_selected': category,
        'questions': questions
    }
    return render(request, "questions.html", context)
'''

def page404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
