from django.contrib import admin
from .models import Employee,Salary,Department
# Register your models here.
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Department)
