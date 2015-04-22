""" Returns a list of potential matches for a student based on the specific sections of a course they
are enrolled in. I.e. the matched students are in the same lecture"""



# Always run this block first so environmental variables are properly loaded 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')


import sys
import django
from queryAndMatchSections import queryAndMatchSections
from queryAndMatchCourses import queryAndMatchCourses
from returnCourseList import returnCourseList
from returnSectionsList import returnSectionsList
from returnStudentData	import returnStudentData


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

def returnMatchesBySection(student_id):
	""" Find a list of students that are in the same section/s as the student. 
	Arguments: student_id 
	Returns a dictionary of matching students. """
	sections_list = returnSectionsList(student_id)

	sections_dict = queryAndMatchSections()

	# for section in sections_list:
	# 	#if no matches found (i.e. returned list of matches contains only the queried user)
	# 	if sections_dict[section] == [str(student_id)]: 
	# 		print "No matches found for section "+str(section)+"."

	# 	else:
	# 		print "Matches for section "+str(section)+":"

	# 	for matched_student in sections_dict[section]:
	# 		if matched_student != str(student_id): #don't list yourself, obviously.
	# 			returnStudentData(matched_student)
	return_dict = {}

	for section in sections_dict:
		if student_id in sections_dict[section]:
			sections_dict[section].remove(student_id)
			return_dict[section] = sections_dict[section]
			

	return return_dict



