""" Returns a list of potential matches for a student based on the specific sections of a course they
are enrolled in. I.e. the matched students are in the same lecture"""
# Always run this block first so environmental variables are properly loaded 

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platypus.settings')

import sys
import django
from matchApp.matchingAlgorithm.queryAndMatchSections import queryAndMatchSections
from matchApp.matchingAlgorithm.queryAndMatchCourses import queryAndMatchCourses
from matchApp.matchingAlgorithm.returnCourseList import returnCourseList
from matchApp.matchingAlgorithm.returnSectionsList import returnSectionsList
from matchApp.matchingAlgorithm.returnStudentData import returnStudentData

# Append parent of the parent directory for cwd to system path               
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

def returnMatchesBySection(student_id):
    """ Find a list of students that are in the same section/s as the student. 
    Arguments: student_id 
    Returns a dictionary of matching students. """
    sections_list = returnSectionsList(student_id)

    sections_dict = queryAndMatchSections()

    return_dict = {}

    for section in sections_dict:
        if student_id in sections_dict[section]:
            sections_dict[section].remove(student_id)
            return_dict[section] = sections_dict[section]
            

    return return_dict