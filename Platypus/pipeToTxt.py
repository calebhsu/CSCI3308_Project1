import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student, User

	
import sys

orig_stdout = sys.stdout
f = file('student.txt', 'w')
sys.stdout = f

for i in Student.objects.raw('SELECT id, course_list, u FROM matchApp_student'):
    print i

sys.stdout = orig_stdout
f.close()
