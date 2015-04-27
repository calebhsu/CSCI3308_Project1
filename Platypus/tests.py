import unittest
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')
import django
from django.test import TestCase
django.setup()
from matchApp.models import User
from matchApp.models import Student
from matchApp.models import Course
from matchApp.models import Section
import time
import matchApp.forms
import matchApp.views
from subprocess import call
from django.test import Client
from django import forms



class TestPlatypus(TestCase):

	def setUp(self):
		self.ml= User(username="Mitch")
		self.lk = User(username="Leo")
		self.ch = User(username = "Caleb")
		self.ml.save()
		self.lk.save()
		self.ch.save()

		self.mitch = Student(user = self.ml)
		self.leo = Student(user= self.lk)
		self.caleb = Student(user= self.ch)
		self.mitch.save()
		self.leo.save()
		self.caleb.save()


		self.soft_tools = Course(title="Soft Tools", course_number= "3308", dept_id = "CSCI" )
		self.algo = Course(title = "algorithims", course_number = "3104", dept_id = "CSCI")
		self.soft_tools.save()
		self.algo.save()

		self.algo1 = Section(class_id = 3104, section_number = "3104001")
		self.soft_tools1 = Section(class_id = 3308, section_number = "3308001")
		self.algo2 = Section(class_id = 3104, section_number = "314002")
		self.algo1.save()
		self.algo2.save()
		self.soft_tools1.save()
		self.algo1.course_title = self.algo
		self.algo2.course_title = self.algo
		self.soft_tools1.course_title = self.soft_tools

		self.mitch.course_list = self.soft_tools.title
		self.leo.course_list = self.soft_tools.title
		self.mitch.course_list = self.algo.title
		self.caleb.course_list = self.soft_tools.title


	def test_Student_with_Course(self):
		self.assertEqual(self.algo.title in self.mitch.course_list, True)
		self.assertEqual(self.algo.title in self.caleb.course_list, False)
		self.assertEqual(self.soft_tools.title in self.leo.course_list, True)
		

	def test_register(self):
		response = self.client.post('/matchApp/register/', {'email' : "platypus@emails.test",
													'username' : "platypus",
													'password' : "platypus123"})
		self.assertEqual(response.status_code == 200, True)
		self.assertEqual(User.objects.filter(username="platypus").exists(), True)

	def test_register_nonUnique_error(self):
		response = self.client.post('/matchApp/register/', {'email' : "platypus@emails.test",
													'username' : "platypus",
													'password' : "platypus123"})
		response = self.client.post('/matchApp/register/', {'email' : "platypus@emails.test",
													'username' : "platypus",
													'password' : "platypus123"})
		self.assertNotEqual(User.objects.filter(username="platypus").count(), 2)

	def test_home_notLoggedIn_error(self):
		response = self.client.get('/matchApp/home/')
		self.assertNotEqual(response.status_code, 200)



if __name__ == '__main__':
	unittest.main()



		

