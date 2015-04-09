#The algorithm will accept from the command line a file that contains strings in this format:
#line 1: student id
#line 2: string literal of course identifiers
import sys

def main():
	inputFile = open(sys.argv[1], 'r')
	studentToMatch = sys.argv[2] #student id of student to match

	numUniqueCourses = 50
	numLines = 0

	for line in inputFile:
		numLines += 1

	matchingMatrix = [["" for x in range(numUniqueCourses)] for x in range(numLines)]
	
	inputFile = open(sys.argv[1], 'r')
	lineNum = 0
	for line in inputFile:
		if (lineNum%2 == 0):
			matchingMatrix[lineNum/2][0] = line.rstrip()
			
		else:
			line = line.rstrip()
			parseLine = line.split(',')

			#sort that shit!
			sortedList = sorted(parseLine)
			index = 1
			for course in sortedList:
				matchingMatrix[lineNum/2][index] = course
				index+=1
		lineNum += 1

	rowToMatch = []

	for row in matchingMatrix:
		if row[0] == studentToMatch:
			rowToMatch = row

	for x in xrange(1,50):
		courseToMatch = 
	for entry in row in matchingMatrix:

			if entry != "":
				for i in xrange(1,50):
					if entry[i] == courseToMatch:
						print entry[0]


if __name__ == '__main__':
	main()