from django.shortcuts import render
from rest_framework import viewsets
from api.models import Nicgangtok,Employee
from api.serializers import NicgangtokSerializer,EmployeeSerializer

# Create your views here.
class NicgangtokViewSet(viewsets.ModelViewSet):
    queryset=Nicgangtok.objects.all()
    serializer_class=NicgangtokSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer