from django.contrib import admin

# Register your models here.
from matchApp.models import Course, Section, Student

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Student)
