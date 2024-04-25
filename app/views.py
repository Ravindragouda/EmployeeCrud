from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def employeeListView(request):
    if request.method=='GET':    
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    

    elif request.method=='POST':
        
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def employeeDetailView(request, pk):
    try:
        employee=Employee.objects.get(pk=pk)
        
    except Employee.DoesNotExist:
        return Response(status=404)



    if request.method=='DELETE':
        employee.delete()
        return Response({"message":"delete success"})

    elif request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method=='PUT':
        
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
   
@api_view(['GET'])
def userListView(request):
    user=User.objects.all()
    serial=UserSerializer(user, many=True)
    return Response(serial.data)