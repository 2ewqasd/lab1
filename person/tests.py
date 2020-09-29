from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Person

class PersonCreateTest(APITestCase):
    def test_create_person(self):
        """
        Ensure that we can create a new person
        """
        url = reverse('person-list')
        data = {"first_name": "Test Gleb",
                "second_name": "Test Bro",
                "years_old": 22,
                "mobile_number": "88005553535"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)