from django.contrib.auth.models import Group
from .models import Employee  # Import your Employee model

def assign_roles():
    # Create custom groups for department heads and employees
    department_head_group, created = Group.objects.get_or_create(name='Department Head')
    employee_group, created = Group.objects.get_or_create(name='Employee')

    # Assign roles to Employee instances
    employee1 = Employee.objects.get(username='employee1_username')  # Replace with actual username or other identifier
    employee2 = Employee.objects.get(username='employee2_username')  # Replace with actual username or other identifier

    # Assign employees to groups based on their roles
    if employee1.is_department_head:  # Add a field in Employee model to identify department heads
        employee1.groups.add(department_head_group)
    else:
        employee1.groups.add(employee_group)

    if employee2.is_department_head:
        employee2.groups.add(department_head_group)
    else:
        employee2.groups.add(employee_group)
