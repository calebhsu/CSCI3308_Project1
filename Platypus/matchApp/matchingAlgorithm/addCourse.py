""" Allows a student to add a course """ 

##############################################################################
# Always run this block first so environmental variables are properly loaded #
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')
##############################################################################

import sys
import django
from queryAndMatchSections import queryAndMatchSections
from queryAndMatchCourses import queryAndMatchCourses
from returnCourseList import returnCourseList
from returnSectionsList import returnSectionsList
from returnStudentData	import returnStudentData

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

def addCourse(student_id, section_id):
	"""Function to add a course to be available on Platypus. 
    Arguments: student_id, and section_id of the course to be added 
	Saves course to database. """
	student = Student.objects.get(user__username=student_id)
	course_list = str(student.course_list)

	course_array = course_list.split(',')
	if section_id in course_array:
		print "Section already in list of enrolled courses"

	else:
		course_array.append(section_id)

	course_list = ""
	for course in course_array:
		if course_list == "":
			course_list+=str(course)
		else:
			course_list += ","+str(course)

	student.course_list = course_list
	student.save()


# def main():
# 	addCourse('bobama', '1300004')


# if __name__ == '__main__':
# 	main()