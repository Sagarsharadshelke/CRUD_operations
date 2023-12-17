from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from.models import emp
# def system_check(request):
#     # return HttpResponse("system check")
#     return render(request,'system.html')

from django.urls import reverse

def home(request):
    return render(request,'home.html')

def success(request):
    return render(request,'success.html')

def add_employee(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        DOB = request.POST.get('DOB')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        
        query = emp(emp_name = emp_name,department = department,salary = salary,DOB = DOB, location = location,gender=gender)
        query.save()
        return render(request,'add_emp_again.html')  # name of the path from urls
    return render(request,'add_employee.html')

def all_emp_data(request):
    data = emp.objects.all()
    return render(request, 'emp_data.html',context={'data':data})




def update_emp(request,id):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        DOB = request.POST.get('DOB')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        
        edit = emp.objects.get(id = id)
        edit.emp_name = emp_name
        edit.department = department
        edit.salary = salary
        edit.DOB = DOB
        edit.location = location
        edit.gender = gender
        edit.save()
        
        return render(request,'UpdateData.html')
    
    
    d = emp.objects.get(id = id)
    context = {'d':d}
    
    return render(request,'UpdateData.html',context=context)
    # pass






def delete_emp(request):
    return render(request,"DeleteData.html")

def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        employee_department = request.POST.get('department')

        try:
            employee = emp.objects.get(id=employee_id, department=employee_department)
            employee.delete()
            return render(request,'delete_emp_again.html')
        except emp.DoesNotExist:
            return HttpResponse("Employee does not exist")
    return HttpResponse("Invalid request")