

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.student.name}'s Profile"
    
class Subjects(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name} - {self.student.name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name