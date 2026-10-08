from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    student = [{ 'name': 'Alice', 'class': '10th'}, { 'name': 'Emly', 'class': '10th'}, {'name': 'Bob', 'class': '11th'}, {'name': 'Charlie', 'class': '12th'}]

    return render(request, 'portfolio/home.html', {'students': student, 'current_time': datetime.now()})