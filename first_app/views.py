from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from first_app import forms
from first_app.models import Student
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    Student_list = Student.objects.order_by('first_name')
     
    return render(request,'first_app/index.html',{'students':Student_list})

def student_form(request):
    form = forms.U
    print(form)
     
    if request.method == "POST":
            form = forms.StudentForm(request.POST)
            if form.is_valid:
                form.save(commit=True)

    return render(request,'first_app/student_form.html',{'student_form': form})

def student_info(request,student_id):
    student_info=Student.objects.get(pk=student_id)
    return render(request,'first_app/student_info.html',{'info':student_info})    

def student_update(request,student_id):
    student_info =Student.objects.get(pk=student_id)
    form=forms.StudentForm(instance=student_info)
    if request.method == "POST":
        form = forms.StudentForm(request.POST,instance=student_info)
        if form.is_valid:
            form.save(commit='True')
            return index(request)
    return render(request,'first_app/student_update.html',{'student_info':form})

def student_delete(request,student_id):
    student =Student.objects.get(pk=student_id).delete()
    
    return render(request,'first_app/student_delete.html',{'delete':"Delete Done"})
