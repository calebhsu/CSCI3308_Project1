#The algorithm will accept from the command line a file that contains strings in this format:
#line 1: student id
#line 2: string literal of course identifiers

import sys
def bubbleSort(inputList):
	#TIME COMPLEXITY: 	O(n**2)
	#SPACE COMPLEXITY: 	O(n) - in place 
	#					O(1) extra space for temp variable

	#Given an unsorted array of size n:
	#bubbleSort works by making n passes from the beginning of the array to the 
	#end of the unsorted portion for the current pass.
	#During each pass, bubbleSort compares each element with the element to its right.
	#If the element being evaluated is greater than the one to its right, the two elements switch places.
	#After each pass completes, the number of unsorted elements should decrease by at least 1.
	#e.g. After pass 1 completes, the highest element should be in place.
	#After pass 2 completes, the second highest element should be in place.
	#(This is why we evaluate on a decreasing subset of the array for every pass)

	#for a length equal to the number of unsorted elements for this pass (decreases every run):
	#repeating for a number of times equal to the number of elements in the array,
	for i in xrange(0,len(inputList)-1):
		#iterate through every element in the array.
		for j in xrange(0,len(inputList)-1):
			#evaluate (compare) and switch as necessary
			if inputList[j] > inputList[j+1]:
				#switch
				temp = inputList[j]
				inputList[j] = inputList[j+1]
				inputList[j+1] = temp

	return inputList

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
			sortedList = bubbleSort(parseLine) #BubbleSort is terrible so I'll implement quicksort or something later. Too tired to do it now
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
	for row in matchingMatrix:
		for entry in row:
			if entry != "":
				for i in xrange(1,50):
					if entry[i] == courseToMatch:
						print entry[0]


if __name__ == '__main__':
	main()