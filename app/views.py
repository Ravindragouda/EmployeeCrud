from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.

def employeeListView(request):
    emp=Employee.objects.all()
    serial=EmployeeSerializer(emp, many=True)

    return JsonResponse(serial.data, safe=False)

