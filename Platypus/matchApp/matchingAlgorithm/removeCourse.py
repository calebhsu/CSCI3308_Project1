"""Allows a student to remove a course from their course list"""

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

def removeCourse(student_id, section_id):
	""" Remove a course from a students course list. 
	Arguments: student_id, section_id of course to be removed.
	Saves the altered couse list. """
	student = Student.objects.get(user__username=student_id)
	course_list = str(student.course_list)

	course_array = course_list.split(',')
	if section_id in course_array:
		course_array.remove(section_id)

	else:
		print("Course is not in list of registered sections")

	course_list = ""
	for course in course_array:
		if course_list == "":
			course_list+=str(course)
		else:
			course_list += ","+str(course)

	student.course_list = course_list
	student.save()

def main():
	removeCourse('bobama', '1300002')


if __name__ == '__main__':
	main()