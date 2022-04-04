# block is forms
from .form import AddArticle, AddLike

#block is model
from .models import Article, Like
from django.contrib.auth.models import User

#servises
from .servises import add_like

#block is django moduls
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.utils import timezone

# Create your views here.

class IndexArticles(ListView):

    template_name = 'articles/index.html'
    context_object_name = 'articles'
    def get_queryset(self):
        return Article.objects.filter(pube_date__lte=timezone.now()).order_by('-pube_date')[:10]


def detail_view(request, article_id):
    form_like = AddLike()
    if request.method == 'POST':
        article = Article
        add_like(article)


def add_article(request, user_id):
    form_class = AddArticle()
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        get_title_article = request.POST['title']
        get_text_article = request.POST['text']
        Article.objects.create(author=user, title=get_title_article, text=get_text_article, pube_date=timezone.now())
        HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'articles/add_article.html', {'form':form_class})
