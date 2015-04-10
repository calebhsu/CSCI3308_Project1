##############################################################################
# Always run this block first so environmental variables are properly loaded #
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')
##############################################################################

import sys
import django
from matchApp.models import Course, Section, Student, User


django.setup()

#Retrieve current working directory so files can be saved to a nested folder
current_directory = os.getcwd()

#Redirect standard output to new students.txt file in specified nested directory (/matchApp/matchingAlgorithm)
sys.stdout = open(current_directory+'/matchApp/matchingAlgorithm/'+'students.txt', 'w')

#Query all rows in Student table; Output return value for each object and its course_list attribute
for i in Student.objects.all():
	print i
	print i.course_list

sys.stdout.close()

#Redirect standard output to new sections.txt file in specified nested directory (/matchApp/matchingAlgorithm)
sys.stdout = file(current_directory+'/matchApp/matchingAlgorithm/'+'sections.txt', 'w')

#Query all rows in Section table; Output return value for each object
for i in Section.objects.all():
	print i

sys.stdout.close()