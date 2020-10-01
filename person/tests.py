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
        url = reverse('person-detail', kwargs={"pk": Person.objects.get().pk})
        self.assertEqual(Person.objects.count(), 1)
        #miss test location. have a quetion
        self.assertEqual(Person.objects.get().first_name, 'Test Gleb')
        self.assertEqual(Person.objects.get().second_name, 'Test Bro')
        self.assertEqual(Person.objects.get().years_old, 22)
        self.assertEqual(Person.objects.get().mobile_number, '88005553535')
    
    def test_wrong_age(self):
        """
        Ensure that wrong age create error
        """
        url = reverse('person-list')
        data = {"first_name": "Test Gleb",
                "second_name": "Test Bro",
                "years_old": "WRONG_AGE",
                "mobile_number": "88005553535"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #i tried to test negative age but i need some advice 
    
    def test_wrong_first_name(self):
        """
        Ensure that wrong first name(more symbols then max_length) create error
        """
        url = reverse('person-list')
        data = {"first_name": "111111111111111111111111111111111111111111111111111111111111111111111",
                "second_name": "Test Bro",
                "years_old": 22,
                "mobile_number": "88005553535"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_second_name(self):
        """
        Ensure that wrong second name(more symbol then max_lenght) create error
        """
        url = reverse('person-list')
        data = {"first_name": "Test Gleb",
                "second_name": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "years_old": 22,
                "mobile_number": "88005553535"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_wrong_number(self):
        """
        Ensure that wrong number(more symbol then max_leght) create error
        """
        url = reverse('person-list')
        data = {"first_name": "Test Gleb",
                "second_name": "Test Bro",
                "years_old": 21,
                "mobile_number": "1111111111111111111111111111111"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    
