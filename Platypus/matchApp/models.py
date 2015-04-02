from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
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
		

	
