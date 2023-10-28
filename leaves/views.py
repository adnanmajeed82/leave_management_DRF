from rest_framework import generics
from .models import Department, Employee, LeaveType, LeaveRequest
from .serializers import DepartmentSerializer, EmployeeSerializer, LeaveTypeSerializer, LeaveRequestSerializer

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LeaveTypeListCreateView(generics.ListCreateAPIView):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

class LeaveRequestListCreateView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
