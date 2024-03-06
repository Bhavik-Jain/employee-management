from rest_framework import serializers
from .models import Employee, Department, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'location']

class EmployeeSerializer(serializers.ModelSerializer):
    dept = DepartmentSerializer()
    role = RoleSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'dept', 'role', 'salary', 'bonus']
