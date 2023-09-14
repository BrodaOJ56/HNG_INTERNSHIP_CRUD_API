from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.exceptions import NotFound

class PersonList(generics.ListCreateAPIView):
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

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer

    def get_object(self):
        lookup_field = 'id'  # Default to looking up by ID

        # Check if the provided 'pk' is a number (ID) or not (name)
        if not self.kwargs['pk'].isdigit():
            lookup_field = 'name'

        try:
            obj = Person.objects.get(**{lookup_field: self.kwargs['pk']})
        except Person.DoesNotExist:
            raise NotFound("Person not found by ID or name.")

        self.check_object_permissions(self.request, obj)
        return obj
