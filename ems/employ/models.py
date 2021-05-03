from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
# Create your models here.


class Department(models.Model):

    departmentID = models.PositiveIntegerField()
    departmentName = models.CharField(max_length=50)
    departmentDate= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.departmentID)


class Salary(models.Model):

    salaryID = models.PositiveIntegerField()
    salaryAmount = models.PositiveIntegerField()
    salaryDate= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.salaryID)

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    profilepic = models.FileField(upload_to='',blank=True)
    usertype = models.CharField(max_length=3,choices=[
                            ('EMP','Employee'),
                            ('MAN','MANAGER'),
                            ('SUP','Superuser'),
                        ],default="EMP")
    gender = models.CharField(max_length=1,choices=[
                            ('M',"Male"),
                            ('F','Female'),
                            ('O','Others'),
                        ],default='M')
    salaryid = models.ForeignKey(Salary,on_delete=models.PROTECT)
    departmentid = models.ForeignKey(Department,on_delete=models.PROTECT)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
