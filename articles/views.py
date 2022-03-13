# block is forms
from .form import AddArticle

#block is model
from .models import Article
from django.contrib.auth.models import User

#block is django moduls
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.utils import timezone

# Create your views here.

class IndexArticles(ListView):

    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(pube_date__lte=timezone.now()).order_by('-pube_date')[:10]



def add_article(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        form_class = AddArticle()
        get_title_article = request.POST['title']
        get_text_article = request.POST['text']
        Article.objects.create(author=user, title=get_title_article, text=get_text_article, pube_date=timezone.now())
        HttpResponseRedirect(reverse('users:index'))
    return render(request, 'articles/add_article.html', {'user':user, 'form':form_class})
