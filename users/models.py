import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=150)
    text = models.TextField(30000)
    pube_date = models.DateTimeField('date time published')
    likes = models.IntegerField(default=0, null=True)
    dislikes = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=10) <= self.pube_date <= now