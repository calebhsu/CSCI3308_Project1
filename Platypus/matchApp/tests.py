
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import django
django.setup()

from matchApp.models import Course, Section, Student
from matchApp.models import User


class TestPlatypus(TestCase):

	def setUp(self):
		self.mitch= Student(username="Mitch")
		self.leo = Student(username="Leo")
		self.mitch.save()
		self.leo.save()
		self.soft_tools = Course(title="Soft Tools", course_number= "3308", dept_id = "CSCI" )
		self.algo = PayGroup(title = "algorithims", course_number = "3104", dept_id = "CSCI")
		self.soft_tools.save()
		self.algo.save()
		self.algo1 = Section(class_id = "CSCI 3104", section_number = "3104001")
		self.soft_tools1 = section(class_id = "CSCI 3308", section_number = "3308001")
		self.algo2 = Section(class_id = "CSCI 3104", section_number = "314002")
		self.algo1.save()
		self.algo2.save()
		self.soft_tools1.save()
		self.algo1.course_title.add(self.algo.title)
		self.algo2.course_title.add(self.algo.title)
		self.soft_tools1.course_title.add(self.soft_tools.title)
		self.mitch.course_list.add(self.soft_tools.title)
		self.leo.course_list.add(self.soft_tools.title)
		self.mitch.course_list.add(self.algo.title)
		self.leo.course_list.add(self.algo.title)
		

