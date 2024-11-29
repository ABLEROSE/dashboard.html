from django.db import models

class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dep_name

class Section(models.Model):
    sec_id = models.AutoField(primary_key=True)
    sec_name = models.CharField(max_length=100)
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.sec_name

class Subsection(models.Model):
    subsection_id = models.AutoField(primary_key=True)
    subsection_name = models.CharField(max_length=100)
    sec_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsection_name

class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=50)

    def __str__(self):
        return self.grade_name

class Employee(models.Model):
    plant_id = models.IntegerField(default=1004)
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    address = models.TextField()
    pan = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    dob = models.DateField()
    doj = models.DateField()
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    education = models.CharField(max_length=50)

    dep_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    sec_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    subsection_id = models.ForeignKey(Subsection, on_delete=models.SET_NULL, null=True)
    grade_id = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     INSERT INTO Employee (
#     emp_id, 
#     name, 
#     address, 
#     pan, 
#     aadhar, 
#     dob, 
#     doj, 
#     sex, 
#     education, 
#     dep_id, 
#     grade_id,
#     sec_id, 
#     subsection_id
#    
# )
# VALUES (
#     101, 
#     'John Doe', 
#     'kaloor', 
#     'ABCDE1234F', 
#     '123456789012', 
#     '1990-01-15', 
#     '2022-06-01', 
#     'Male', 
#     'Btech', 
#     1, 
#     2,
#     3, 
#     4
# );

