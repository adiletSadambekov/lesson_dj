from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Article(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=150)
    text = models.TextField(30000)
    pube_date = models.DateTimeField('date time published')
    looks = models.IntegerField(default=0)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.pube_date <= now
    
    @property
    def total_likes(self):
        return self.likes.count()