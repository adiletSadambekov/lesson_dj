import datetime
from rest_framework import serializers
from .models import Questions

class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

question = Questions(question_text='question text', pub_date=datetime.datetime.now())

print(question)