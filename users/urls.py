from os import name
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexArticles.as_view(), name='index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('<user_id>/add_article/', views.add_article, name='add_article')
]