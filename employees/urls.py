from django.urls import path

from employees.views import (
    ListEmployeesAPIView,
    CreateEmployeeAPIView,
    DeleteEmployeeAPIView,
)

app_name = "employees"

urlpatterns = [
    path("get_employees/", ListEmployeesAPIView.as_view()),
    path("post_employee/", CreateEmployeeAPIView.as_view()),
    path("delete_employee/<int:pk>/", DeleteEmployeeAPIView.as_view()),
]
