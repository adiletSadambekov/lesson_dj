import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from .models import Questions, Choice


def create_question(question_text, days):
    pube_date = timezone.now() + datetime.timedelta(days=days)
    return Questions.objects.create(question_text=question_text, pub_date=pube_date)


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=10)
        future_question = Questions(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_width_old_question(self):

        time = timezone.now() - datetime.timedelta(days=5, seconds=1)
        old_question = Questions(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_width_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=50, seconds=59)
        recent_question = Questions(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIindexViewTests(TestCase):

    def no_question(self):
        self.client = Client()
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        question = create_question(question_text='This is test past question', days=-30)
        self.client = Client()
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        self.client = Client()
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


    def test_future_question_and_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        self.client = Client()
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        self.client = Client()
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )