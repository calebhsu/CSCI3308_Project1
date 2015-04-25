# Platypus

Managing students based on academic need and extracurricular interest as the preferred social media platform of academia.

Live site: http://leokim89.pythonanywhere.com/matchApp/

### Contributors
Paige Alleman, Caleb Hsu, Leo Kim, Mitchell Lewis, Tommy Wagner

##AutoDoc HTML Navigation: 
To use the HTML Doxygen output, download the HTML folder under the AutoDocumentation section in the repository. Run index.html from that file to use a clickableversion of the auto documentation. Alternatively, view the refman.pdf file in the same AutoDocumentation section. 

## Repository Organization
```
└── CSCI3308_Project1
    ├── Platypus                            # Contains the Platypus project
    |   ├── AutoDocumentation               # Folder containing documentation
    |   |   ├── html                        # Contains Doxygen-generated HTML files for online documentation
    |   |   ├── latex                       # Documentation in latex format
    |   |   ├── AutoDocConfiguration_1  
    |   |   └── refman.pdf                  # Generated documentation pdf file.
    |   ├── Platypus                        # Contains files that determine Platypus settings
    |   ├── matchApp                        # Contains main source code
    |   |   ├── matchingAlgorithm           # Contains course and section match code
    |   |   ├── templatetags
    |   |   ├── admin.py
    |   |   ├── forms.py
    |   |   ├── models.py                   # Contains database models
    |   |   ├── tests.py     
    |   |   ├── urls.py
    |   |   └── views.py                    # Contains most of structural source code
    |   ├── static                          # Static tools used with Django framework 
    |   |   ├── bootstrap           
    |   |   |   ├── css
    |   |   |   ├── fonts
    |   |   |   └── js
    |   |   ├── css
    |   |   |   └── styles.css              # CSS file for Platypus website
    |   |   └── images                      # Contains stock image for webpage background
    |   ├── templates/matchApp              # HTML for Platypus website
    |   |   ├── addcourses.html
    |   |   ├── classpage.html
    |   |   ├── home.html
    |   |   ├── login.html
    |   |   └── register.html
    |   ├── db.sqlite3
    |   ├── manage.py
    |   ├── populate.py
    ├── Project Information                 # Contains files for weekly project submissions in Markdown
    |   ├── ERDiagram.png
    |   ├── projectPlan.png
```

## Using GitHub
The following instructions assume the user has

1. A GitHub account
2. Git installed on machine
    - Note to Windows users: during setup, make sure to select "Run Git From Windows Command Prompt"
    - To configure,
```sh
$ git config --global user.name "usernamehere"
$ git config --global user.email youremail@example.com
```

##### One-Time Actions 
These only need to be done once:
- Fork CSCI3308_Project1 repository on GitHub 
- Clone fork to computer using 
```sh
$ git clone [git-repo-url]
```

### Development
##### Pull, Commit, Push
- Always pull before committing for fewer conflicts between master and fork! 
    - see "Keeping Your Fork Up-to-Date"
- If ready to contribute code modifications to master, return to level of CSCI3308_Project1 directory, then
```sh
$ git status                            # display unadded paths
$ git add file                     		# add file or path to file
$ git status                            # check if path is added
$ git commit -m "messagehere"           # commit to fork
$ git push                              # add modified fork to GitHub
```
    - Note that the commit message uses single quotes on Linux systems
    
- Go to GitHub and create pull request from the fork
    - Click the green button in the upper left

##### Keeping Your Fork Up-To-Date
The following is necessary to keep your fork up-to-date with changes in the master. 
- Add remote from original repository into fork
```sh
# This is a one-time action
$ cd locationonmachine/CSCI3308_Project1           
$ git remote add upstream [git-repo-url]    
```
- Fetch all branches of remote into remote tracking branch
```sh
$ git fetch upstream                     
```
- Update fork from original to keep up with changes
```sh
$ git pull upstream master
```

## Team Rules & Guidelines
1. Communicate intentions to learn/accomplish a goal of the project to other members.
2. Communicate intentions to accomplish class assignments so that we can work together.
3. Establish weekly meetings for in-person communications. Otherwise communicate clearly that no meeting is needed.
4. Project guidelines for each step will be clearly shown to all members.
5. If a great resource is found for project-related learning, it will be posted to the other team members for reading.
6. Sync regularly with GitHub repository and alert team members to changes.
