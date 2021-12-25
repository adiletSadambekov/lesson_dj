from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Questions

# Create your views here.
class IndexView(generic.ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):

    model = Questions
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    
    model = Questions
    template_name = 'polls/result.html'


def vote(request, question_id):

    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/voteform.html', {'question': question, 'error_messege': "You did't select a choice."})
    
    else:
        selected_choice.choice_set.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))