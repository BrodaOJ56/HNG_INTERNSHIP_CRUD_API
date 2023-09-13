
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        if not isinstance(value, str) or len(value) <= 1 or value.isdigit():
            raise serializers.ValidationError("Name must be a valid non-numeric string with at least two characters.")
        return value
