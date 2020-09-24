from .models import Person
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Person.objects.all()
    serializer_class = UserSerializer