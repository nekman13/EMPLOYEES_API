from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from employees.models import Employee
from employees.serializers import CreateEmployeeSerializer, GetEmployeeSerializer


# Create your views here.


class ListEmployeesAPIView(ListAPIView):
    """Вывод списка сотрудников"""

    serializer_class = GetEmployeeSerializer
    queryset = Employee.objects.all()


class CreateEmployeeAPIView(CreateAPIView):
    """Добавление сотрудников"""

    serializer_class = CreateEmployeeSerializer
    queryset = Employee.objects.all()


class DeleteEmployeeAPIView(DestroyAPIView):
    """Удаление сотрудника"""

    serializer_class = CreateEmployeeSerializer
    queryset = Employee.objects.all()
