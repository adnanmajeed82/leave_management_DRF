from django.urls import path
from .views import CompanyListCreateView, EmployeeListCreateView, LeaveTypeListCreateView, LeaveRequestListCreateView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('leave-types/', LeaveTypeListCreateView.as_view(), name='leave-type-list-create'),
    path('leave-requests/', LeaveRequestListCreateView.as_view(), name='leave-request-list-create'),
]
