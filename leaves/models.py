from django.db import models
from datetime import date
 

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.CharField(max_length=300)
    ApprovedBY = models.ForeignKey(Department, on_delete=models.CASCADE)
    casual_leave_balance = models.IntegerField(default=0)
    sick_leave_balance = models.IntegerField(default=0)
    annual_leave_balance = models.IntegerField(default=0)
    def __str__(self):
        return self.user

class LeaveType(models.Model):
    LeaveName = models.CharField(max_length=50)
    def __str__(self):
        return self.LeaveName

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved_by_hr = models.BooleanField(default=False)
    # Add other fields like status, comments, etc.


    def calculate_leave_balance(self, leave_type):
        today = date.today()
        leave_requests = LeaveRequest.objects.filter(
            employee=self,
            leave_type=leave_type,
            start_date__lte=today,
            end_date__gte=today,
        )
        total_leave_days = sum([(request.end_date - request.start_date).days + 1 for request in leave_requests])
        if leave_type == 'casual':
            self.casual_leave_balance = total_leave_days
        elif leave_type == 'sick':
            self.sick_leave_balance = total_leave_days
        elif leave_type == 'annual':
            self.annual_leave_balance = total_leave_days
        self.save()

     