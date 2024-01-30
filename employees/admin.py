from django.contrib import admin

from employees.models import Employee, Department


# Register your models here.

admin.site.register(Employee)

admin.site.register(Department)

#
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     fields = fields = [
#         "id",
#         "first_name",
#         "last_name",
#         "role",
#         "salary",
#         "hire_date",
#         "date_of_birth",
#         "department",
#     ]
#     search_fields = ["__all__"]
#
#
# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     fields = ["__all__"]
#     search_fields = ["__all__"]
