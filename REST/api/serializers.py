from rest_framework import serializers, validators

from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model=Student
        fields=['name','roll','city']
        
