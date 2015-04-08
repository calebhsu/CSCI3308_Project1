import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platypus_project.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student

def populate():
	csci_1300 = add_course("Computer Science 1: Starting Computing", "CSCI", 1300)
	csci_1310 = add_course("Computer Science 1: Starting Computing - Experienced", "CSCI", 1310)
	csci_2270 = add_course("Computer Science 2: Data Structures", "CSCI", 2270)
	csci_2400 = add_course("Computer Systems", "CSCI", 2400)
	csci_2820 = add_course("Linear Algebra with Computer Science Applications", "CSCI", 2820)
	csci_2824 = add_course("Discrete Structures", "CSCI", 2824)
	csci_3104 = add_course("Algorithms", "CSCI", 3104)
	csci_3155 = add_course("Principles of Programming Languages", "CSCI", 3155)
	csci_3308 = add_course("Software Development Methods and Tools", "CSCI", 3308)
	csci_3753 = add_course("Operating Systems", "CSCI", 3753)

	add_section(1300001, csci_1300, 001)
	add_section(1300002, csci_1300, 002)
	add_section(1300003, csci_1300, 003)

	add_section(1310001, csci_1310, 001)
	add_section(1310002, csci_1310, 002)
	add_section(1310003, csci_1310, 003)

	add_section(2270001, csci_2270, 001)
	add_section(2270002, csci_2270, 002)
	add_section(2270003, csci_2270, 003)

	add_section(2400001, csci_2400, 001)
	add_section(2400002, csci_2270, 002)
	add_section(2400003, csci_2270, 003)

	add_section(2820001, csci_2820, 001)
	add_section(2820002, csci_2820, 002)
	add_section(2820003, csci_2820, 003)

	add_section(2824001, csci_2824, 001)
	add_section(2824002, csci_2824, 002)
	add_section(2824003, csci_2824, 003)

	add_section(3104001, csci_3104, 001)
	add_section(3104002, csci_3104, 002)
	add_section(3104003, csci_3104, 003)

	add_section(3155001, csci_3155, 001)
	add_section(3155002, csci_3155, 002)
	add_section(3155003, csci_3155, 003)

	add_section(3308001, csci_3308, 001)
	add_section(3308002, csci_3308, 002)
	add_section(3308003, csci_3308, 003)

	add_section(3753001, csci_3753, 001)
	add_section(3753002, csci_3753, 002)
	add_section(3753003, csci_3753, 003)

	sample_course_list_1 = "1300001,2270002,2400001"
	sample_course_list_2 = "1300001,2270001,2400003"
	sample_course_list_3 = "1300002,2270002,2400003"
	sample_course_list_4 = "1300003,2270001,2400003"

	add_student(900000001, "Barack", "Obama", "bobama", "password123", "bobama@colorado.edu", sample_course_list_1,"", "")
	add_student(900000002, "Vladimir", "Putin", "vputin", "password123", "vputin@colorado.edu", sample_course_list_2, "", "")
	add_student(900000003, "Dear", "Leader", "kimjeongun", "password123", "dearleader@colorado.edu", sample_course_list_3, "", "")
	add_student(900000004, "Doctor", "Zoidberg", "zoidberg", "password123", "zoidberg@colorado.edu", sample_course_list_4, "", "")

def add_course(title, dept_id, course_number):
	new_course = Course.objects.get_or_create(title = title)[0]
	new_course.dept_id = dept_id
	new_course.course_number = course_number

	new_course.save()

	return new_course

def add_section(class_id, course_title, section_number):
	new_section = Section.objects.get_or_create(class_id = class_id)[0]
	new_section.course_title = course_title
	new_section.section_number = section_number

	new_section.save()

	return new_section


def add_student(student_id, first_name, last_name, user_id, password, email_address, course_list, view_url, pic_url):
	new_student = Student.objects.get_or_create(student_id = student_id)[0] #get_or_create method returns a tuple, where element 0 is the object
	new_student.first_name = first_name
	new_student.last_name = last_name
	new_student.user_id = user_id
	new_student.password = password
	new_student.email_address = email_address
	#new_student.course_table = course_table
	new_student.course_list = course_list
	new_student.view_url = view_url
	new_student.pic_url = pic_url

	new_student.save()

	return new_student


if __name__ == '__main__':
	print "populating matchApp databases"
	populate()