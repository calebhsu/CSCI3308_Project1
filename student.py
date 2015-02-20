class Student:
	'Student object with relevant attributes'
	def __init__(self, sid, lastName, firstName, year, major, classList):
		self.sid = sid
		self.lastName = lastName
		self.firstName = firstName
		self.year = year
		self.major = major
		self.classList = classList

	#getter functions
	def getSID(self):
		print(self.sid)
	
	def getName(self):
		print(self.lastName," ",self.firstName)
	
	def getLast(self):
		print(self.lastName)

	def getFirst(self):
		print(self.firstName)
	
	def getYear(self):
		print(self.year)

	def getMajor(self):
		print(self.major)

	def getClassList(self):
		print(self.classList)

	def getAll(self):
		print 'SID:',self.sid,'\nName:', self.lastName+',',self.firstName,'\nYear:',self.year,'\nMajor:',self.major,'\nClasses: ',self.classList	
	
	#setter functions
	def addClass(self, newClass):
                self.classList.append(newClass)

	
	#def removeClass(self, someClass):
		#search array for someClass, if found set that element in the array to None; else print error]
			
			
	def setSID(self, sid):
		self.sid = sid
	
	def setLast(self, lastName):
		self.lastName = lastName

	def setFirst(self, firstName):
		self.firstName = firstName

	def setYear(self, year):
		self.year = year
	
	def setMajor(self):
		self.major = major
