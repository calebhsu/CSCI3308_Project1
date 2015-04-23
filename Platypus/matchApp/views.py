"""
Basic functionality of the application, including login and user authentication. Each view handles 

"""
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from matchApp.models import Student, Course, Section, User
from matchApp.forms import UserForm

from django.core.management import call_command


# Import from child directory matchingAlgorithm
""" import matching algorithm from child directory"""
from matchApp.matchingAlgorithm.returnCourseList import returnCourseList
from matchApp.matchingAlgorithm.returnMatchesByCourse import returnMatchesByCourse
from matchApp.matchingAlgorithm.returnMatchesBySection  import returnMatchesBySection
from matchApp.matchingAlgorithm.addCourse import addCourse

def index(request):
    """ Request context of request. Context contains information such as client's machine details. 
    Construct dictionary to pass context to the templates, so that the correct page renders.
    Return rendered response to send to client. 
    """
   
    context = RequestContext(request)

    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {}

    
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

            userData = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, userData)
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
    print(user.username)
    course_list = returnCourseList(user.username) 
    print(course_list)
    context_dict = {'course_list':course_list}

    return render_to_response('matchApp/home.html', context_dict, context)

@login_required
def classpage(request):
    """Render the specific class page of the user that logs in."""
    context = RequestContext(request)

    user = request.user
    course_dict = returnMatchesByCourse(user.username)
    sections_dict = returnMatchesBySection(user.username)

    student_dict = {}
    for student in Student.objects.all():
        student_dict[student.user.username]=student.user.email

    context_dict = {'course_dict':course_dict, 'sections_dict':sections_dict, 'student_dict':student_dict}

    return render_to_response('matchApp/classpage.html', context_dict, context)

@login_required
def user_logout(request):
    """Allow user to exit application and log out. Returns to login screen."""
    logout(request)

    return HttpResponseRedirect('/matchApp/')

@login_required
def addcourses(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    course_list = Course.objects.all()
    context_dict = {'course_list':course_list}
    return render_to_response('matchApp/addcourses.html', context_dict, context)

@login_required
def selectsection_CSCI1300(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=1300)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI1300.html', context_dict, context)

@login_required
def selectsection_CSCI1310(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=1310)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI1310.html', context_dict, context)

@login_required
def selectsection_CSCI2270(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=2270)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI2270.html', context_dict, context)

@login_required
def selectsection_CSCI2400(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=2400)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI2400.html', context_dict, context)

@login_required
def selectsection_CSCI2820(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=2820)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI2820.html', context_dict, context)

@login_required
def selectsection_CSCI2824(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=2824)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI2824.html', context_dict, context)

@login_required
def selectsection_CSCI3104(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=3104)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI3104.html', context_dict, context)

@login_required
def selectsection_CSCI3155(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=3155)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI3155.html', context_dict, context)

@login_required
def selectsection_CSCI3308(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=3308)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI3308.html', context_dict, context)

@login_required
def selectsection_CSCI3753(request):
    context = RequestContext(request)
    user=request.user
    sections_list = Section.objects.filter(course_title__course_number=3753)
    context_dict = {'sections_list':sections_list}
    return render_to_response('matchApp/selectsection_CSCI3753.html', context_dict, context)



@login_required
def add1300001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1300001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add1300002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1300002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add1300003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1300003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add1310001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1310001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add1310002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1310002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add1310003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '1310003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add2270001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2270001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2270002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2270002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2270003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2270003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add2400001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2400001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2400002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2400002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2400003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2400003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add2820001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2820001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2820002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2820002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2820003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2820003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add2824001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2824001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2824002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2824002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add2824003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '2824003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add3104001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3104001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3104002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3104002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3104003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3104003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add3155001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3155001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3155002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3155002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3155003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3155003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add3308001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3308001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3308002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3308002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3308003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3308003')
    return HttpResponseRedirect('/matchApp/home')

@login_required
def add3753001(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3753001')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3753002(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3753002')
    return HttpResponseRedirect('/matchApp/home')
@login_required
def add3753003(request):
    context = RequestContext(request)
    user=request.user
    username = str(user.username)
    addCourse(user.username, '3753003')
    return HttpResponseRedirect('/matchApp/home')


