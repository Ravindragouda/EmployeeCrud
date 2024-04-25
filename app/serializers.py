from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
    
class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=30)
    first_name=serializers.CharField()
    last_name=serializers.CharField()
   