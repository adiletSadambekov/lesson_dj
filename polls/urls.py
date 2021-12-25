from typing import Pattern
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<pk>/result/', views.ResultView.as_view(), name='result'),
    path('<question_id>/vote/', views.vote, name='vote'),
]