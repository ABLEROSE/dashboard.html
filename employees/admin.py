from django.contrib import admin
from django.forms import DateInput, ModelForm
from .models import Department, Section, Subsection, Grade, Employee

# Custom Form for Employee Model with DD-MM-YYYY date format
class EmployeeAdminForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'dob': DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
            'doj': DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dob'].input_formats = ['%d-%m-%Y']
        self.fields['doj'].input_formats = ['%d-%m-%Y']

# Custom Employee Admin
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm

admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Grade)
admin.site.register(Employee, EmployeeAdmin)
