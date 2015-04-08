from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
class Student(models.Model):
		user = models.ForeignKey(User)
		courses = models.CharField(max_length = 4, default = "")
		
		
		def __unicode__(self):
			return self.user.username
			
class Course(models.Model):
	name = models.CharField(max_length = 200, default = "")
	number = models.CharField(max_length = 4, default = "")
	students = models.ManyToManyField(Student)
	
	def __unicode__(self):
		return self.number
'''

class Course(models.Model):
	title = models.CharField(max_length=64, default="")
	dept_id = models.CharField(max_length=4, default="")
	course_number = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title	

class Section(models.Model):
	class_id = models.IntegerField(default=0)
	course_title = models.ForeignKey(Course, null=True)
	#course_title = models.CharField(max_length=64, default="")
	section_number = models.IntegerField(default=0)

	def __unicode__(self):
		return self.class_id	

class Student(models.Model):
	student_id = models.IntegerField(default=0)
	first_name = models.CharField(max_length=64, default="")
	last_name = models.CharField(max_length=64, default="")

	user_id = models.CharField(max_length=64, default="")
	password = models.CharField(max_length=64, default="")

	email_address = models.CharField(max_length=128, default="")

	course_list = models.CharField(max_length=1024, default="")

	#view_url = models.URLField()
	#pic_url = models.URLField()

	def __unicode__(self):
		return self.student_id