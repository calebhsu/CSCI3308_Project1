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

def returnMatchesByCourse(student_id):
	course_list = returnCourseList(student_id)

	course_dict = queryAndMatchCourses()

	for course in course_list:
		course_id = course[0:8]
		#print course_title
		#if no matches found (i.e. returned list of matches contains only the queried user)
		if course_dict[course_id] == [str(student_id)]: 
			print "No matches found for course "+str(course)+"."

		else:
			print "Matches for:\n"+str(course)

		for matched_student in course_dict[course_id]:
			if matched_student != str(student_id): #don't list yourself, obviously.
				returnStudentData(matched_student)


# def main():
# 	returnMatchesByCourse(900000001)

# if __name__ == '__main__':
# 	main()
	
