from django.shortcuts import render
from .models import Employee, Department, Section, Subsection, Grade


def dashboard(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    context = {
        'employees': employees,
        'departments': departments,
        'employee_count': employees.count(),
    }
    return render(request, 'dashboard.html', context)
