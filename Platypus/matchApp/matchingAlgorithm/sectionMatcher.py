#pass two command-line args to matchingAlgorithm:
#file with unique section ID on each line
#file with format as follows:
#	<student ID>
#	<comma-separated string of courses associated with that student>

import sys

sectionsFile = open(sys.argv[1],'r')
studentsFile = open(sys.argv[2],'r')

sectionsDict = {}
dictSize = 0
#sectionsArray = []
for line in sectionsFile:
	line = line.rstrip()
	sectionsDict[line] = []
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
			sectionsDict[newArray[index]].append(newArray[0])
			# print(newArray[index])
			# print(sectionsDict[newArray[index]])
			
		newline = ""

	lineNum+=1

for key in sectionsDict:
	print ("Section number: "+key)
	print ("Enrolled students: "+str(sectionsDict[key]))