from student import Student
from getStudentInfo import getStudentInfo

def buildStudentList(): #return an array of Student objects
	studentList = []
	askInsert = input("Add a new student? (1)Yes (2)No ")
	while (askInsert!=1 and askInsert!=2):
		askInsert = input("\nInvalid Selection. Add a new student? (1)Yes (2)No ")
	if askInsert == 1:
		studentList.append(getStudentInfo())
	else:
		return studentList
	askContinue = input("\nAdd another student? (1)Yes (2)No ")
	while (askContinue!=1 and askContinue!=2):
		askContinue = input("\nInvald Selection. Add another Student? (1)Yes (2)No ")

	while (askContinue == 1):
		studentList.append(getStudentInfo())
		askContinue = input("\nAdd another student? (1)Yes (2)No ")
		while (askContinue!=1 and askContinue!=2):
			askContinue = input("\nInvalid Selection. Add another student? (1)Yes (2)No ") 
	
	if (askContinue == 2):
		return studentList


def main():
	studentList = buildStudentList()
	size = len(studentList)
	for i in range (0, size):
		studentList[i].getAll()
		print "\n"


if __name__ == "__main__":
	main()	
