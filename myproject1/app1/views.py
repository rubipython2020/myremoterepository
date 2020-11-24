from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Employee_details

# Create your views here.
def home(request):
    return render(request,'home.html')


def create(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        dept=request.POST.get('dept')
        address=request.POST.get('address')

        details=Employee_details(
            fname=fname,
            lname=lname,
            mobile=mobile,
            email=email,
            dept=dept,
            address=address
        )

        details.save()
        context = {'employeedata': Employee_details.objects.all()}
        return render(request, 'studentcreate.html', context)

    context = {'employeedata': Employee_details.objects.all()}
    return render(request, 'studentcreate.html', context)


'''def update(request):
    context={'employeedata' : Employee_details.objects.get()}
    return render(request, 'update.html',context)'''




def update_view(request,id):
    context = {'employeedata': Employee_details.objects.get(id=id)}
    return render(request, 'update.html', context)


def update_view_save(request,id):
    context=Employee_details.objects.get(id=id)
    context.fname=request.POST.get('fname')
    context.lname=request.POST.get('lname')
    context.mobile=request.POST.get('mobile')
    context.email=request.POST.get('email')
    context.dept=request.POST.get('dept')
    context.address=request.POST.get('address')
    context.save()
    return redirect('/')


def delete(request,id):
    employee=Employee_details.objects.get(id=id)
    employee.delete()
    return redirect('/')