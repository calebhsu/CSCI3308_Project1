""" Organizes information from database according to students and their courses"""
# Always run this block first so environmental variables are properly loaded #
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')


import sys
import django

# Append parent of the parent directory for cwd to system path               #
os.getcwd()
os.chdir('..')
os.chdir('..')
directory = os.getcwd()

if directory in sys.path:
	pass
else:
	sys.path.append(directory)


from matchApp.models import Course, Section, Student, User
django.setup()

def queryAndMatchCourses():
	""" Create a hashtable that saves course numbers as keys and arrays of enrolled students as values. 
	Query all sections in the database.
	Save each section number from course_list string into an array.
	Extract department ID and first four chars of section id.
	Returns the course dictionary.
	"""
	#Create a hashtable that will save course numbers as keys and arrays of enrolled students as values
	courseDict = {}

	#Query all sections in the database;
	#Extract department ID and first four chars of section id;
	#Concatenate the two strings and save as key
	for section in Section.objects.all():
		deptID = str(section.course_title.dept_id).rstrip()
		sectionString = str(section).rstrip()[0:4]

		courseID = deptID+sectionString
		courseDict[courseID] = []

	#Query all students in the database;
	#Save every section number from course_list string into an array;
	#For each section number in the array:
	#	Query database for class with identical section number;
	#	Query database for department ID for section with that number;
	#	Concatenate the two values (coercing as strings and slicing first four chars of section number) to reconstruct courseID
	#	Hash in to dict with extracted courseID, and append student to the hashed array
	for student in Student.objects.all():
		courseString = str(student.course_list).rstrip()
		courseArray = courseString.split(',')
		for course in courseArray:
			classID = Section.objects.get(class_id=course)
			deptID = classID.course_title.dept_id
			courseID = str(deptID)+str(classID)[0:4]

			courseDict[courseID].append(str(student))

	return courseDict


	# # For Production Code: redirect output to appropriate files in the views folder #
	# for key in courseDict:
	# 	print ("Course ID: "+key)
	# 	print ("Enrolled students: "+str(courseDict[key]))


# def main():
# 	queryAndMatchCourses()

# if __name__ == '__main__':
# 	main()