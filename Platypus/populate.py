"""
Connects the information in the database to Platypus
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student
from matchApp.models import User

def populate():
    """ Add courses and sections to database, including catalog course pages.
    Key Variables: 
    csci_#### -- courses added 
    sample_course_list_# -- list of sample courses with which to test the app. 
    """

	csci_1300 = add_course("Computer Science 1: Starting Computing", "CSCI", 1300, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/1300-computer-science-1-starting-computing")
	csci_1310 = add_course("Computer Science 1: Starting Computing - Experienced", "CSCI", 1310, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/1310-computer-science-1-starting-computing-experienced")
	csci_2270 = add_course("Computer Science 2: Data Structures", "CSCI", 2270, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/2270-computer-science-2-data-structures")
	csci_2400 = add_course("Computer Systems", "CSCI", 2400, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/2400-computer-systems")
	csci_2820 = add_course("Linear Algebra with Computer Science Applications", "CSCI", 2820, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/2820-linear-algebra-computer-science-applications")
	csci_2824 = add_course("Discrete Structures", "CSCI", 2824, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/2824-discrete-structures")
	csci_3104 = add_course("Algorithms", "CSCI", 3104, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/3104-algorithms")
	csci_3155 = add_course("Principles of Programming Languages", "CSCI", 3155, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/3155-principles-programming-languages")
	csci_3308 = add_course("Software Development Methods and Tools", "CSCI", 3308, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/3308-softwaredevelopment-methods-and-tools")
	csci_3753 = add_course("Operating Systems", "CSCI", 3753, "http://www.colorado.edu/catalog/2015-16/courses/engr/b-csci/3753-operating-systems")

	add_section(1300001, csci_1300, 101)
	add_section(1300002, csci_1300, 102)
	add_section(1300003, csci_1300, 103)

	add_section(1310001, csci_1310, 101)
	add_section(1310002, csci_1310, 102)
	add_section(1310003, csci_1310, 103)

	add_section(2270001, csci_2270, 101)
	add_section(2270002, csci_2270, 102)
	add_section(2270003, csci_2270, 103)

	add_section(2400001, csci_2400, 101)
	add_section(2400002, csci_2270, 102)
	add_section(2400003, csci_2270, 103)

	add_section(2820001, csci_2820, 101)
	add_section(2820002, csci_2820, 102)
	add_section(2820003, csci_2820, 103)

	add_section(2824001, csci_2824, 101)
	add_section(2824002, csci_2824, 102)
	add_section(2824003, csci_2824, 103)

	add_section(3104001, csci_3104, 101)
	add_section(3104002, csci_3104, 102)
	add_section(3104003, csci_3104, 103)

	add_section(3155001, csci_3155, 101)
	add_section(3155002, csci_3155, 102)
	add_section(3155003, csci_3155, 103)

	add_section(3308001, csci_3308, 101)
	add_section(3308002, csci_3308, 102)
	add_section(3308003, csci_3308, 103)

	add_section(3753001, csci_3753, 101)
	add_section(3753002, csci_3753, 102)
	add_section(3753003, csci_3753, 103)

	sample_course_list_1 = "1300001,2270002,2400001"
	sample_course_list_2 = "1300001,2270001,2400003"
	sample_course_list_3 = "1300002,2270002,2400003"
	sample_course_list_4 = "1300003,2270001,2400003"

	add_student(900000001, "Barack", "Obama",  "password123", "bobama@colorado.edu", sample_course_list_1,"", "")
	add_student(900000002, "Vladimir", "Putin", "password123", "vputin@colorado.edu", sample_course_list_2, "", "")
	add_student(900000003, "Dear", "Leader", "password123", "dearleader@colorado.edu", sample_course_list_3, "", "")
	add_student(900000004, "Doctor", "Zoidberg", "password123", "zoidberg@colorado.edu", sample_course_list_4, "", "")

def add_course(title, dept_id, course_number, catalog_page):
    """ Add a new course to the database for use"""
	new_course = Course.objects.get_or_create(title = title)[0]
	new_course.dept_id = dept_id
	new_course.course_number = course_number
	new_course.catalog_page = catalog_page

	new_course.save()

	return new_course

def add_section(class_id, course_title, section_number):
    """ Add a new section of a class, useful because there may be multiple sections of, say, CSCI1300 """
	new_section = Section.objects.get_or_create(class_id = class_id)[0]
	new_section.course_title = course_title
	new_section.section_number = section_number

	new_section.save()

	return new_section

def add_student(student_id, first_name, last_name, password, email_address, course_list, view_url, pic_url):
    """ Enable creation of a new user, Return the newly added student.""" 
	new_User = User.objects.get_or_create(email = email_address)[0]
	new_User.first_name = first_name
	new_User.last_name = last_name
	new_User.password = password
	new_User.username = student_id
	new_User.save()
	
	new_student = Student.objects.get_or_create(user = new_User)[0] #get_or_create method returns a tuple, where element 0 is the object
	
	
	new_student.course_list = course_list
	new_student.view_url = view_url
	new_student.pic_url = pic_url

	new_student.save()

	return new_student


if __name__ == '__main__':
	print("Populating matchApp databases")
	populate()
