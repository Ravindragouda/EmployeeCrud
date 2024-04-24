from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
# Create your views here.

def employeeListView(request):
    emp=Employee.objects.all()
    serial=EmployeeSerializer(emp, many=True)

    return JsonResponse(serial.data, safe=False)

def userListView(request):
    user=User.objects.all()
    serial=UserSerializer(user, many=True)
    return JsonResponse(serial.data, safe=False)