#pass two command-line args to matchingAlgorithm:
#file with unique section ID on each line
#file with format as follows:
#	<student ID>
#	<comma-separated string of courses associated with that student>


#STILL NEEDS:
#Method to append department code to front of each extracted course ID
#Possible solutions:
#Query db for associated dept id in pipeToText.py

import sys

coursesFile = open(sys.argv[1],'r')
studentsFile = open(sys.argv[2],'r')

coursesDict = {}
dictSize = 0

for line in coursesFile:
	line = line.rstrip()
	line = line[0:4]
	coursesDict[line] = []
	dictSize += 1

lineNum = 0
newline = ""
newArray = []
for line in studentsFile:
	line = line.rstrip()
	if (lineNum%2 == 0):
		newline += line
	elif (lineNum%2 == 1):
		newline += ","+line
		newArray = newline.split(',')

		for index in xrange(1,len(newArray)):
			newArray[index] = newArray[index][0:4]
			# print newArray[index]
			coursesDict[newArray[index]].append(newArray[0])
			
		newline = ""

	lineNum+=1

for key in coursesDict:
	print ("Course number: "+key)
	print ("Enrolled students: "+str(coursesDict[key]))