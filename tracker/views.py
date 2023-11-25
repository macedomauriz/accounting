from django.http import HttpResponse

from .models import Character
from .serializers import CharacterSerializer
from rest_framework import permissions
from rest_framework import viewsets


# pure Django example
def detail(request, number):
    return HttpResponse("You're looking at question %s." % number)


class CharactersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
