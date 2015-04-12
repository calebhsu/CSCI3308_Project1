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

def returnSectionsList(student_id):
	queried_student = Student.objects.get(user__username=student_id) #use "__" to access foreign key attributes
	course_array = str(queried_student.course_list).split(',')
	return course_array


def main():
	print returnSectionsList(900000001)

if __name__ == '__main__':
	main()

