from django.db import models


class Person(models.Model):
    """
    Class with fields
    """
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=100)
    years_old = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=17)