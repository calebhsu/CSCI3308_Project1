"""
Basic functionality of the application, including login and user authentication. 
"""
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from matchApp.models import Student, Course, Section, User
from matchApp.forms import UserForm


# Import from child directory matchingAlgorithm
""" import matching algorithm from child directory"""
from matchApp.matchingAlgorithm.returnCourseList import returnCourseList



def index(request):
    """ Request context of request. Context contains information such as client's machine details. 
    Construct dictionary to pass context to the templates, so that the correct page renders.
    Return rendered response to send to client. 
    """
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

def register(request):
    """ Boolean value checks to see if registration was sucessful by the user."""
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

def user_login(request):
    """ Determines activity level of the user and reacts accordingly to correct/incorrect login information."""
    # Get relevant info if HTTP post
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checks if username/password combo is valid
        user = authenticate(username=username, password=password)

        # Checks if user with matching info was found
        if user:
            if user.is_active:
                # If valid & active, send to homepage
                login(request, user)
                return HttpResponseRedirect('/matchApp/home')
            else:
                # An inactive account was used
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided
            print("Invalid login details")
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'matchApp/login.html', {})

@login_required
def home(request):
    """Render the specific home page of the user that logs in."""
    context = RequestContext(request)

    user = request.user
    print user.username
    #obviously, we can't hard-code the user id in.
    #When user authentication gets figured out, replace 900000001 with the user id variable
    course_list = returnCourseList(user.username) 
    print(course_list)
    context_dict = {'course_list':course_list}

    return render_to_response('matchApp/home.html', context_dict, context)

@login_required
def classpage(request):
    """Render the specific class page of the user that logs in."""
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('matchApp/classpage.html', context_dict, context)

@login_required
def user_logout(request):
    """Allow user to exit application and log out. Returns to login screen."""
    logout(request)

    return HttpResponseRedirect('/matchApp/')