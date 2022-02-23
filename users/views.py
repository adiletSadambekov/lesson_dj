from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from .models import Article
from django.utils import timezone
from .form import RegisterUsers, AddArticle
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
class IndexArticles(ListView):

    template_name = 'users/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(pube_date__lte=timezone.now()).order_by('-pube_date')[:10]


def profile(request):
    return render(request, 'users/profile.html')




class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    success_url = '/acconts/login/'
    form_class = RegisterUsers


def add_article(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form_class = AddArticle()
    if request.method == 'POST':
        get_title_article = request.POST['title']
        get_text_article = request.POST['text']
        new_article = Article.objects.create(author=user, title=get_title_article, text=get_text_article, pube_date=timezone.now())
        HttpResponseRedirect(reverse('users:index'))
    return render(request, 'users/add_article.html', {'user':user, 'form':form_class})
    