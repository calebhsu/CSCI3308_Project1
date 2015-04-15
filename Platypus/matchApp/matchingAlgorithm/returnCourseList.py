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

def returnCourseList(student_id):
	queried_student = Student.objects.get(user__username=student_id) #use "__" to access foreign key attributes
	course_array = str(queried_student.course_list).split(',')

	return_array = []
	for course in course_array:
		queried_course = Section.objects.get(class_id=course)
		dept_id = str(queried_course.course_title.dept_id)
		course_number = str(queried_course.course_title.course_number)
		course_title = str(queried_course.course_title)
		return_array.append(dept_id+course_number+" - "+course_title)

	return return_array




# def main():
# 	for course in returnCourseList(900000001):
# 		print course

# if __name__ == '__main__':
# 	main()

