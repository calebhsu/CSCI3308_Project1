""" Organizes information from the database according to students and their specific sections of courses."""
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


def queryAndMatchSections():
	"""Create a hashtable that saves section numbers as keys and arrays of enrolled students as values. 
	Querey all rows in the section and student tables. Add the student ID to to the array hashed by the directory for each course
	in which the student is enrolled. 
	Return a dictionary of the sections. 
	"""
	#Create a hashtable that will save sections numbers as keys and arrays of enrolled students as values
	sectionsDict = {}

	#Query all rows in Section table;
	#For each section, create an entry with the section number as the key and an empty array as the value
	for section in Section.objects.all():
		sectionString = str(section).rstrip()
		sectionsDict[sectionString] = []
		
	#Query all rows in Student table; 
	#Concatenate the SID and course_list attributes of each student object, coercing return values to strings;
	#Save comma-separated entries of the concatenated string into an array;
	#For every course the student is enrolled in, add the SID to the array hashed by the dictionary
	for student in Student.objects.all():
		sid = str(student).rstrip()
		courseString = str(student.course_list).rstrip()
		concatenate = sid+','+courseString
		row = concatenate.split(',')

		for index in xrange(1,len(row)):
			sectionsDict[row[index]].append(row[0])

	return sectionsDict

	# #################################################################################
	# # For Production Code: redirect output to appropriate files in the views folder #
	# for key in sectionsDict:
	# 	print ("Section number: "+key)
	# 	print ("Enrolled students: "+str(sectionsDict[key]))
	# #################################################################################

# def main():
# 	queryAndMatchSections()

# if __name__ == '__main__':
# 	main()