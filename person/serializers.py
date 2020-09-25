from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Person

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'first_name', 'second_name', 'years_old','mobile_number']