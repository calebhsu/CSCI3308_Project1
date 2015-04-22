"""
Contains information about the various classes used in Platypus
"""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    """ Named course, but essentially creates a class for the classes available on platypus.
    Attributes: 
    title -- name of course 
    dept_id -- department prefix, example CSCI 
    course_number -- example 1300 for CSCI 1300 
    catalog_page --  link to the page where the course is located in the CU course catalog
    """  
    title = models.CharField(max_length=64, default="")
    dept_id = models.CharField(max_length=4, default="")
    course_number = models.IntegerField(default=0)
    catalog_page = models.URLField(default="http://www.colorado.edu/catalog/2015-16/courses")

    def __unicode__(self):
        return unicode(self.title)  

class Section(models.Model):
    """ Differentiate between different sections of the same class. 
    Attirbutes: 
    class_id -- example CSCI 1300
    course_title -- name of course, passed as argument for constructor for new section creation
    section_number -- unique section number for class section
    """ 
    class_id = models.IntegerField(default=0)
    course_title = models.ForeignKey(Course, null=True)
    section_number = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.class_id)   

class Student(models.Model):
    """ Class to handle a user. 
    Note: student now returns username, username is assigned to student_id 
    Attributes: 
    user -- user identity unique to each student
    course_list -- list of courses specific to the student/user
    """ 
    user = models.ForeignKey(User)

    course_list = models.CharField(max_length=1024, default="")

    def __unicode__(self):
        return unicode(self.user.username) #UPDATED student now returns username, username will be assigned to student_id
