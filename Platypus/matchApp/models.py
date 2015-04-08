from django.db import models


class Course(models.Model):
	title = models.CharField(max_length=64)
	dept_id = models.CharField(max_length=4, default="")
	course_number = models.IntegerField(default=0)

	def __unicode__(self):
		return unicode(self.title)


class Section(models.Model):
	class_id = models.IntegerField(default=0)
	course_title = models.ForeignKey(Course, null=True)
	#course_title = models.CharField(max_length=64, default="")
	section_number = models.IntegerField(default=0)

	def __unicode__(self):
		return unicode(self.class_id)

class Student(models.Model): #class ClassName(<some_class>) <-- allows you to inherit from some_class
	student_id = models.IntegerField()
	first_name = models.CharField(max_length=64, default="")
	last_name = models.CharField(max_length=64, default="")

	user_id = models.CharField(max_length=64, default="")
	password = models.CharField(max_length=64, default="")

	email_address = models.CharField(max_length=128, default="")
	
	
	#course_table = models.ForeignKey(Section)
	#I have no clue how to make this shit work, so we'll do it the brute-force way.
	#sql doesn't allow you to store a multivalue tuple/list/array whatever as a value.
	#so, we'll just save them as string literals and do happy python shit in the background.

	course_list = models.CharField(max_length=1024, default="")


	view_url = models.URLField()
	pic_url = models.URLField()

	def __unicode__(self):
		return unicode(self.student_id)





