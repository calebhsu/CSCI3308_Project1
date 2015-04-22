""" Gets the specific data associated with a student user, i.e. a username, name, and email. 
"""


# Always run this block first so environmental variables are properly loaded
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import sys
import django


# Append parent of the parent directory for cwd to system path    
os.getcwd()
os.chdir('..')
os.chdir('..')
directory = os.getcwd()

if directory in sys.path:
	pass
else:
	sys.path.append(directory)

from matchApp.models import Course, Section, Student, User
django.setup()


# The contents of this function will be highly variable, and must be tailored
# to the actual content needed by the HTML coders. For now, include all the
# functionality that might be needed, and comment out. 
# Uncomment required fields later as needed by the HTML/front-end team.

def returnStudentData(student_id):
	"""Find information associated with a student user. 
	Arguments: student_id. 
	Returns the attributes of the student user. """
	queried_student = Student.objects.get(user__username=student_id) #use "__" to access foreign key attributes
	username = queried_student.user.username
	name = str(queried_student.user.first_name)+" "+str(queried_student.user.last_name)
	email = queried_student.user.email

	print "Username:\t"+username
	print "Name:\t\t"+name
	print "Email:\t\t"+email+"\n"

	return queried_student

