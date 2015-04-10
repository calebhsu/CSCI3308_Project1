import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student, User

	
import sys

orig_stdout = sys.stdout
student_file = file('students.txt', 'w')
sys.stdout = student_file

for i in Student.objects.all():
	print i
	print i.course_list

sys.stdout = orig_stdout
student_file.close()

orig_stdout = sys.stdout
section_file = file('sections.txt', 'w')
sys.stdout = section_file

for i in Section.objects.all():
	print i

sys.stdout = orig_stdout
section_file.close()