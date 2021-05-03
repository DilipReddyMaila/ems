from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import datetime
from .models import Employee,Salary,Department

# def handle_uploaded_file(f):
#     with open('ems/static/media/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

@login_required(login_url='/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('verify'))

def verify(request):

    if request.method == 'POST' :
            username = request.POST['Username']
            password = request.POST['Password']
            user = authenticate(request,username=username,password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)

                    userdata = User.objects.get(username=username)
                    return HttpResponseRedirect(reverse('profile'))
                else:
                     return render(request,'employ/index.html',{'error':"User is not active"})
            else:
                return render(request,'employ/index.html',{'error':"Invalid Credentials"})
    else:
        return render(request,'employ/index.html',{'error':''})

@login_required(login_url='/')
def emp_create(request):
    if request.user.employee.usertype != "EMP" :
        if request.method == "POST":

            ppic = request.FILES.getlist('Profilepic')

            print(ppic)
            # for i in ppic:
            #     ppic = i
            #     break
            user =User.objects.create(username=request.POST['Username'],
                    email=request.POST['Email'])
            user.password = make_password(request.POST['Password'])
            user.save()
            userdata = Employee.objects.create(user=user,designation=request.POST['Designation'],
                    usertype=request.POST['Usertype'],gender=request.POST['Gender'],
                    address=request.POST['Address'],profilepic=ppic[0],
                    salaryid=Salary.objects.get(salaryID=request.POST['SalaryID']),departmentid=Department.objects.get(departmentID=request.POST['DepartmentID']))

            userdata.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request,'employ/employee_form.html',{'user':request.user,'deplist':Department.objects.all(),'sallist':Salary.objects.all()})
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def profile(request):
    return render(request,'employ/profile.html',{'user':request.user})
@login_required(login_url='/')
def salaryview(request):
    return render(request,'employ/view_sal.html',{'sal':Salary.objects.all(),'user':request.user})
@login_required(login_url='/')
def departmentview(request):
    return render(request,'employ/view_dep.html',{'dep':Department.objects.all(),'user':request.user})
@login_required(login_url='/')
def updatedep(request,pk):
    if request.user.employee.usertype == "SUP" :
        if request.method == "POST":
            depart = Department.objects.get(departmentID=pk)
            depart.departmentName = request.POST['DepartmentName']
            depart.save()
            return HttpResponseRedirect(reverse('view_dep'))
        return render(request,'employ/dep_update.html')
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def deletedep(request,pk):
    if request.user.employee.usertype == "SUP" :
        depart = Department.objects.get(departmentID=pk)
        depart.delete()
        return HttpResponseRedirect(reverse('view_dep'))
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def createdep(request):
    if request.user.employee.usertype == "SUP" :
        if request.method == "POST":

            depart = Department.objects.create(departmentID=request.POST['DepartmentID'],departmentName=request.POST['DepartmentName'],
                                                departmentDate=datetime.datetime.now())
            depart.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request,'employ/depart_form.html')
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def createsal(request):
    if request.user.employee.usertype == "SUP" :
        if request.method=="POST":

            salary = Salary.objects.create(salaryID=request.POST['SalaryID'],salaryAmount=request.POST['SalaryAmount'],salaryDate=datetime.datetime.now())
            salary.save()
            return HttpResponseRedirect(reverse('profile'))
        return render(request,'employ/sal_form.html')
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def updatesal(request,pk):
    if request.user.employee.usertype == "SUP" :
        if request.method == "POST":
            sal = Salary.objects.get(salaryID=pk)
            sal.salaryAmount = request.POST['SalaryAmount']
            sal.save()
            return HttpResponseRedirect(reverse('view_sal'))
        return render(request,'employ/sal_update.html')
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def deletesal(request,pk):
    if request.user.employee.usertype == "SUP" :
        sal = Salary.objects.get(salaryID=pk)
        sal.delete()
        return HttpResponseRedirect(reverse('view_sal'))
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def viewemp(request):
    if not request.user.employee.usertype == "SUP":
        emp = Employee.objects.filter(departmentid=request.user.employee.departmentid,usertype="EMP")
        return render(request,'employ/emp_view.html',{'emp':emp,'user':request.user})
    else:
        return render(request,'employ/emp_view.html',{'emp':Employee.objects.all(),'user':request.user})
@login_required(login_url='/')
def empupdate(request,pk):
    if request.user.employee.usertype != "EMP" :
        if request.method=="POST":
            emp = Employee.objects.get(user_id=pk)
            emp.designation = request.POST['designation']
            emp.usertype = request.POST['usertype']
            emp.salaryid = Salary.objects.get(salaryID=request.POST['salaryid'])
            emp.departmentid = Department.objects.get(departmentID=request.POST['departmentid'])
            emp.save()
            return HttpResponseRedirect(reverse('emp_view'))
        emp = Employee.objects.get(user_id=pk)
        return render(request,'employ/emp_update.html',{'user':request.user,'emp':emp,'deplist':Department.objects.all(),'sallist':Salary.objects.all()})
    return  render(request,'employ/no_access.html')
@login_required(login_url='/')
def empdelete(request,pk):
    if request.user.employee.usertype != "EMP" :
        user = User.objects.get(id = pk)
        user.delete()
        return HttpResponseRedirect(reverse('emp_view'))
    return  render(request,'employ/no_access.html')
