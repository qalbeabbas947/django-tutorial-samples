from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Student
from time import timezone
# Create your views here.
def home(request):
    student = [{ 'name': 'Alice', 'class': '10th'}, { 'name': 'Emly', 'class': '10th'}, {'name': 'Bob', 'class': '11th'}, {'name': 'Charlie', 'class': '12th'}]

    return render(request, 'portfolio/home.html', {'students': student, 'current_time': datetime.now()})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'portfolio/student_list.html', {'students': students})

def contact_view(request):
    return render(request, 'portfolio/contact.html')

def contact_submit(request):
    if(  request.method == 'POST' and request.POST.get('name') and request.POST.get('email') and request.POST.get('message')):

        if request.method == 'POST':
            name_val = request.POST.get('name')
            email_val = request.POST.get('email')
            message_val = request.POST.get('message')
            
            Contact.objects.create(name=name_val, email=email_val, message=message_val, create_at=datetime.now())
            
            return HttpResponse(f"Contact submitted successfully! Name: {name_val}, Email: {email_val}, Message: {message_val}")
        if request.method == 'GET':
            name_val = request.GET.get('name')
            email_val = request.GET.get('email')
            message_val = request.GET.get('message')

            Contact.objects.create(name=name_val, email=email_val, message=message_val, create_at=datetime.now())
        
            return HttpResponse(f"Contact submitted successfully! Name: {name_val}, Email: {email_val}, Message: {message_val}")
    else:
        return redirect('contact')    
