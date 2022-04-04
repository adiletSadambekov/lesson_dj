from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexArticles.as_view(), name='index'),
    path('<user_id>/add_article/', views.add_article, name='add_article'),
    path('<pk>/detail_article/', views.DetatilViewArticle.as_view(), name='detail_view')
]