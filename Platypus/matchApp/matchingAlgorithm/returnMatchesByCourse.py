""" Returns a list of potential matches for the student based on the courses they are enrolled in. """


# Always run this block first so environmental variables are properly loaded 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import sys
import django
from matchApp.matchingAlgorithm.queryAndMatchSections import queryAndMatchSections
from matchApp.matchingAlgorithm.queryAndMatchCourses import queryAndMatchCourses
from matchApp.matchingAlgorithm.returnCourseList import returnCourseList
from matchApp.matchingAlgorithm.returnSectionsList import returnSectionsList
from matchApp.matchingAlgorithm.returnStudentData import returnStudentData


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

def returnMatchesByCourse(student_id):
	""" Find a list of students that are taking the same course/s as the student. 
	Arguments: student_id 
	Returns dictionary of matching students. """
	course_list = returnCourseList(student_id)

	course_dict = queryAndMatchCourses()

	
	return_dict = {}

	for course in course_dict:
		if student_id in course_dict[course]:
			course_dict[course].remove(student_id)
			return_dict[course] = course_dict[course]

	# print return_dict

	#key: course; value: student
	return return_dict


def main():
	returnMatchesByCourse('bobama')

if __name__ == '__main__':
	main()
	
