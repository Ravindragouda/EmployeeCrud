from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=30)
    phone=serializers.IntegerField()


    def create(self, validated_data):
        print("create method called")
        return Employee.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        newemp=Employee(**validated_data)
        newemp.id=employee.id;
        newemp.save()
        return newemp

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=30)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=30)
    first_name=serializers.CharField()
    last_name=serializers.CharField()
   