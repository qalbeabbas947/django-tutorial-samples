from django.contrib import admin
from portfolio.models import Student
from portfolio.models import Profile
from portfolio.models import Subjects
from portfolio.models import Contact

#admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Subjects)
admin.site.register(Contact)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city')
    search_fields = ('name', 'city', 'age')
    list_filter = ('city',)

# Register your models here.
