from rest_framework import serializers

from employees.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор департамента"""

    class Meta:
        model = Department
        fields = ["id", "name", "location", "created_date"]


class GetEmployeeSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Employee.ROLES, source="get_role_display")
    department = DepartmentSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "role",
            "salary",
            "hire_date",
            "date_of_birth",
            "department",
            "tasks",
        ]


class CreateEmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор сотрудника"""

    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "role",
            "salary",
            "hire_date",
            "date_of_birth",
            "department",
            "tasks",
        ]
