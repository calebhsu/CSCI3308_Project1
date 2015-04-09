import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platypus_project.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student

	
import sys

orig_stdout = sys.stdout
f = file('student.txt', 'w')
sys.stdout = f

for i in Student.object.raw('SELECT student_id, course_list FROM models.py'):
    print i

sys.stdout = orig_stdout
f.close()
