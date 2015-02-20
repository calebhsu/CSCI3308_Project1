#to import classes from another .py file in the directory,
#create an empty file called __init__.py and import using from <name of .py file> import <name of class>
from student import Student

#to use regex, import re module and use re.match() function
import re

def getStudentInfo():
	classList = []

	askID = raw_input("Enter Student ID: ")
	#while (len(sid)!=9): #could also use regex
	testID = re.match("[1,9]\d{8}",askID) #not sure what the actual id format is, but using 9XXXXXXXX
	if testID: #if true
		sid = askID
	else:
		print "Wrong, motherfucker!"
		#too tired to implement correction loop. do it later.
		#seriously, REMEMBER TO FINISH THIS
			
	#print "Invalid Student ID. Please enter valid Student ID: "
	#Enter confirmation loop to validate SID

	lastName = raw_input("Enter Last Name: ")
	
	firstName = raw_input("Enter First Name: ")
	
	askYear = input("Select Year: (1)Freshman (2)Sophomore (3)Junior (4)Senior: ")
	if (askYear == 1):
			year = "Freshman"
		
	elif (askYear == 2):
			year = "Sophomore"
		
	elif (askYear == 3):
			year = "Junior"
		
	elif (askYear == 4):
			year = "Senior"
		
	else:
		while (askYear != 1 and askYear != 2 and askYear != 3 and askYear != 4):
			askYear = input("Invalid Selection. Select Year: (1)Freshman (2)Sophomore (3)Junior (4)Senior: ")
	
	major = raw_input("Enter Major: ")
	#The list of available options should be populated by a database	

	askClass = input("Add classes now? (1)Yes (2)No: ")
	while(askClass != 1 and askClass != 2):
		askClass = input("Invalid Selection. Add classes now? (1)Yes (2)No: ")	
	#Same as with major, the classes should be imported from a databse	
	

	#Right now the classes are being saved into an array...
	#How do you save this shit to a database??	
	while(askClass==1):
		classList.append(raw_input("Enter class name: "))
		askClass = input("Add another class? (1)Yes (2)No: ")
		while(askClass != 1 and askClass != 2):
			askClass = input("Invalid Selection. Add another class? (1)Yes (2)No: ")
	
	newStudent = Student(sid, lastName, firstName, year, major, classList)
	return newStudent

def main():
	newStudent = getStudentInfo()
	newStudent.getAll()

if __name__ == "__main__":
	main()
