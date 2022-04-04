from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import Like

def add_like(article, user):
    article_type = ContentType.objects.get_for_model(article)
    like, is_create = Like.objects.get_or_create(content_type=article_type, object_id=article.id, user=user)
    return like


def remove_like(article, user):
    article_type = ContentType.objects.get_for_model(article)
    Like.objects.filter(content_type=article_type, object_id=article.id, user=user.id).delete()


def is_fan(article, user) -> bool:
    if not user.is_authenticated:
        return False
    article_type = ContentType.objects.get_for_model(article)
    like = Like.objects.filter(content_type=article_type, object_id=article.id, user=user.id)
    return like.exists()


def get_fans(article):
    article_type = ContentType.objects.get_for_model(article)
    return User.objects.filter(likes__content_type=article_type, likes__article_id=article.id)
