from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from matchApp.models import Student, Course, Section, User
from matchApp.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

##############################################################################
# Import from child directory matchingAlgorithm
from matchApp.matchingAlgorithm.returnCourseList import returnCourseList
##############################################################################


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('matchApp/login.html', context_dict, context)

def home(request):
    context = RequestContext(request)

    #obviously, we can't hard-code the user id in.
    #When user authentication gets figured out, replace 900000001 with the user id variable
    course_list = returnCourseList(900000001) 
    print(course_list)
    context_dict = {'course_list':course_list}

    return render_to_response('matchApp/home.html', context_dict, context)

def classpage(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('matchApp/classpage.html', context_dict, context)

def register(request):
    #context = RequestContext(request)
    # Boolean value for telling the template whether registration was successful.
    registered = False

    # If HTTP POST, we're interested in processing form data
    if request.method == 'POST':
        # Attempt to get raw form info
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            userData = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            userData.set_password(userData.password)
            userData.save()

            # Make new account.
            student_user = Student(user=userData)
            student_user.save()

            # Tells template registration was successful
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    return render(request, 
            'matchApp/register.html', 
            {'user_form': user_form, 'registered': registered} )