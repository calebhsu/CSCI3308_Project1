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

sys.path.append(directory)
##############################################################################

from matchApp.models import Course, Section, Student, User
django.setup()


#Create a hashtable that will save sections numbers as keys and arrays of enrolled students as values
#Initialize size counter to calculate number of entries cheaply
sectionsDict = {}
dictSize = 0

#Query all rows in Section table; Output return value for each object
for section in Section.objects.all():
	sectionString = str(section).rstrip()
	sectionsDict[sectionString] = []
	dictSize += 1



#Query all rows in Student table; Output return value for each object and its course_list attribute
for student in Student.objects.all():
	sid = str(student).rstrip()
	courseString = str(student.course_list).rstrip()
	concatenate = sid+','+courseString
	row = concatenate.split(',')

	for index in xrange(1,len(row)):
		sectionsDict[row[index]].append(row[0])

#################################################################################
# For Production Code: redirect output to appropriate files in the views folder #
for key in sectionsDict:
	print ("Section number: "+key)
	print ("Enrolled students: "+str(sectionsDict[key]))
#################################################################################
