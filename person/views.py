from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonCreate(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdate(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonDelete(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer