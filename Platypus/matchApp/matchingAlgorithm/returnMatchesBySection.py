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

sys.path.append(directory)
##############################################################################

from matchApp.models import Course, Section, Student, User
django.setup()

def returnMatchesBySection(student_id):
	sections_list = returnSectionsList(student_id)

	sections_dict = queryAndMatchSections()

	for section in sections_list:
		#if no matches found (i.e. returned list of matches contains only the queried user)
		if sections_dict[section] == [str(student_id)]: 
			print "No matches found for section "+str(section)+"."

		else:
			print "Matches for section "+str(section)+":"

		for matched_student in sections_dict[section]:
			if matched_student != str(student_id): #don't list yourself, obviously.
				returnStudentData(matched_student)


# def main():
# 	returnMatchesBySection(900000001)

# if __name__ == '__main__':
# 	main()
	
