""" Returns what specific sections of a course a student is enrolled in. """

##############################################################################
# Always run this block first so environmental variables are properly loaded #
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')
##############################################################################

import sys
import django

##############################################################################
# Append parent of the parent directory for cwd to system path               #
os.getcwd()
os.chdir('..')
os.chdir('..')
directory = os.getcwd()

if directory in sys.path:
	pass
else:
	sys.path.append(directory)
##############################################################################

from matchApp.models import Course, Section, Student, User
django.setup()

def returnSectionsList(student_id):
	"""Queries the database for information about sections regarding a specific student. 
	Arguments: student_id 
	Returns the sections associated with the student. """
	queried_student = Student.objects.get(user__username=student_id) #use "__" to access foreign key attributes
	sections_array = str(queried_student.course_list).split(',')
	return sections_array


# def main():
# 	print returnSectionsList(900000001)

# if __name__ == '__main__':
# 	main()

