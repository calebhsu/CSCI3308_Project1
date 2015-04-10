###################################################################
# TO DO:
# Consider incorporating pipeToText.py into this code.
# This is only possible if environmental variables can be properly imported.

#pass two command-line args to matchingAlgorithm:
#file with unique section ID on each line
#file with format as follows:
#	<student ID>
#	<comma-separated string of courses associated with that student>

import sys

#Command-line arguments:
#Argument 1: sections.txt
#Argument 2: students.txt
sectionsFile = open(sys.argv[1],'r')
studentsFile = open(sys.argv[2],'r')

#Create a hashtable that will save sections numbers as keys and arrays of enrolled students as values
#Initialize size counter to calculate number of entries cheaply
sectionsDict = {}
dictSize = 0

for line in sectionsFile:
	line = line.rstrip() #remove newline chars and other problematic whitespace
	sectionsDict[line] = [] #initialize value to an empty array
	dictSize += 1


lineNum = 0 #Used to determine whether current line contains SID field or course_list string 

tempLine = "" #Required for inexpensive string manipulation

for line in studentsFile:
	line = line.rstrip() #remove newline chars and other problematic whitespace

	#If even, current line contains SID field
	if (lineNum%2 == 0):
		tempLine += line

	#If odd, current line contains course_list string
	elif (lineNum%2 == 1):
		tempLine += ","+line #e.g. "900000001,1300001,2827003,3380001"
		tempArray = tempLine.split(',') #save comma-separated entries into an array

		#Hash into the dict with current section as the key;
		#Append to current SID to the hashed array
		for index in xrange(1,len(tempArray)):
			sectionsDict[tempArray[index]].append(tempArray[0])

		#Reset tempLine to empty string for next pass of SID and course_list entries
		tempLine = ""

	lineNum+=1

#################################################################################
# For Production Code: redirect output to appropriate files in the views folder #
for key in sectionsDict:
	print ("Section number: "+key)
	print ("Enrolled students: "+str(sectionsDict[key]))
#################################################################################
