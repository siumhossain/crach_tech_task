from django.test import TestCase

# Create your tests here.
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from question.models import Question
from question.models import FavoriteQuestion
from question.models import ReadQuestion

class QuestionInfoViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        #create users
        self.user_1 = User.objects.create(
            display_name="sium",
            phone="01905192544",
            email="s@yahoo.com",
            username="sium",
            password=make_password('hellodear')
        )
        self.user_2 = User.objects.create(
            display_name="sium2",
            phone="01905192544",
            email="s2@yahoo.com",
            username="sium2",
            password=make_password('hellodear')
        )

        #create question
        self.question1 = Question.objects.create(
            question='What is the capital of France?',
            option=[
                {
                    'option1':"Sydney",
                    'option2':"Newyork",
                    'option3':"PARIS",
                    'option4':"FRANCE",
                    'option5':"CTG",
                }
            ],
            answer=2,
            explain='Paris is the capital of France.'
        )

        self.question2 = Question.objects.create(
            question='What is 2 + 2?',
            option=[
                {
                    'option1':1,
                    'option2':2,
                    'option3':3,
                    'option4':4,
                    'option5':5,
                }
            ],
            answer=4,
            explain='2 + 2 equals 4.'
        )
        self.fvrt_question = FavoriteQuestion.objects.create(
            user_id=self.user_1,
            question_id=self.question1
        )
        self.read_question = ReadQuestion.objects.create(
            user_id=self.user_2,
            question_id=self.question2
        )

    def test_get_questions(self):
        url = reverse('question_info-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_favorite_question(self):
        url = reverse('question_info-list')
        response = self.client.get(url, {'favorite': 'true'})
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(
            entry['question'] == self.fvrt_question.question_id.question
            for entry in response_data['results']
        ))

    def test_get_unfavorite_question(self):
        url = reverse('question_info-list')
        response = self.client.get(url, {'unfavorite': 'true'})
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(
            entry['question'] == self.read_question.question_id.question
            for entry in response_data['results']
        ))

    def test_get_read_question(self):
        url = reverse('question_info-list')
        response = self.client.get(url, {'read': 'true'})
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(
            entry['question'] == self.read_question.question_id.question
            for entry in response_data['results']
        ))

    def test_get_unread_question(self):
        url = reverse('question_info-list')
        response = self.client.get(url, {'unread': 'true'})
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(
            entry['question'] == self.fvrt_question.question_id.question
            for entry in response_data['results']
        ))
