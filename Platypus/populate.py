import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')
import django
django.setup()

from matchApp.models import User
from matchApp.models import Student
from matchApp.models import Course


def populate():
	
	#create User info
	Mitch = User(username = "Mitch123123", first_name = "Mitchell" , last_name = "Lewis" , email = "mitchell.lewis@colorado.edu")
	Mitch.set_password("MitchIsCool")
	Mitch.save()
	
	frog = User(username = "KermitDaFrog", first_name = "Kermit", last_name = "Frog", email = "kermitTheFrog@colorado.edu")
	frog.set_password("ItAintEasyBeingGreen")
	frog.save()
	
	Jedi = User(username  = "Obiwan", first_name = "Obiwan", last_name = "Kenobi", email = "obiwan.kenobi@colorado.edu")
	Jedi.set_password("ForceBWithU")
	Jedi.save()
	
	
	# create student object, put in User info
	m = Student(user = Mitch, courses = "3308")
	m.save()
	
	kermit = Student(user = frog, courses = "3155")
	kermit.save()
	
	Obiwan = Student(user = Jedi, courses = ["3155", "3308", "1111"])
	Obiwan.save()
	
	
	#create soft tools class
	soft_Tools = Course(name = "Soft Tools" , number = "3308")
	soft_Tools.save()
	
	ppl = Course(name = "Principles of Programming Languages", number = "3155")
	ppl.save()
	
	testClass = Course(name = "Test Class", number = "1111")
	testClass.save()



if __name__ == '__main__':
    print "Starting Platupus population script..."
    populate()
    print "Done!"
