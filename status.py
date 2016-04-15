#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#import modules for CGI handling
import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
status = form.getvalue('status')
username = form.getvalue('username')
#username = "test2"

if(status == None or status.isspace()):
    print "Content-Type: text/html;charset=utf-8"
    print

    print "<html>"
    print "<head>"
    print   "<title>Dashboard</title>"
    print   "</head>"
    print   "<body>"

    print     "<h1 style='color:Navy;'>Welcome to Your Dashboard %s!</h1>" % username

    print     "<h3>Menu: </h3>"
    print     "<form action=\"welcome.html\">"
    print      "<button>Logout</button>"
    print     "</form>"
    print     "<form action=\"makefriends.py\">"
    print       "<button>Make a Friend</button>"
    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username

    print     "</form>"
    print     "<form action=\"seefriends.c\">"
    print       "<button>See a Friend</button>"
    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username

    print     "</form>"

    print     "<br>"
    print     "<br>"
    print     "<br>"

    print     "<h3>*** Please enter a non-blank status update.</h3>"
    print     "<form name=\"form\" action=\"status.py\" method=\"get\">"
    print       "Status Update: <input type=\"text\" name=\"status\">"
    print       "<input type=\"submit\" value=\"Update Status\" />"

    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username
    print     "</form>"

    print     "<br> <h2><u>Status Updates from You and Your Friends</u></h2>"
    usernameAndFriends = None

    with open("friends.txt") as f:
        for line in f:
            if(line.split(' ', 1)[0] == username):
                usernameAndFriends = line
                break
    if(usernameAndFriends != None): 
	usernameList = usernameAndFriends.split()
        # print(usernameList)

        i=0
    	for line in reversed(list(open("status.txt"))):
        	i+=1
        	for user in usernameList:
	            	if(line.split(' ', 1)[0] == user):
		                print "<p>" + line + "</p>"
        	if(i>19):
        	    	break

    print   "</body>"
    print "</html>"










else:
    f = open('status.txt','a')
    f.write(username + ' ' + status + '\n')
    f.close()

    print "Content-Type: text/html;charset=utf-8"
    print

    print "<html>"
    print "<head>"
    print   "<title>Dashboard</title>"
    print   "</head>"
    print   "<body>"

    print     "<h1 style='color:Navy;'>Welcome to Your Dashboard %s!</h1>" % username

    print     "<h3>Menu: </h3>"
    print     "<form action=\"welcome.html\">"
    print      "<button>Logout</button>"
    print     "</form>"
    print     "<form action=\"makefriends.py\">"
    print       "<button>Make a Friend</button>"
    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username
    print     "</form>"
    print     "<form action=\"seefriends.cgi\">"
    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username

    print       "<button>See a Friend</button>"
    print     "</form>"

    print     "<br>"
    print     "<br>"
    print     "<br>"

    print     "<form name=\"form\" action=\"status.py\" method=\"get\">"
    print       "Status Update: <input type=\"text\" name=\"status\">"
    print       "<input type=\"submit\" value=\"Update Status\" />"

    print       "<input type = \"hidden\" name=\"username\" value=\"%s\">" % username
    print     "</form>"

    print     "<br> <h2><u>Status Updates from You and Your Friends</u></h2>"
    usernameAndFriends = None

    with open("friends.txt") as f:
        for line in f:
            if(line.split(' ', 1)[0] == username):
                usernameAndFriends = line
                break
    if(usernameAndFriends != None):
	usernameList = usernameAndFriends.split()
        # print(usernameList)

	i = 0
    	for line in reversed(list(open("status.txt"))):
        	i+=1
        	for user in usernameList:
            		if(line.split(' ', 1)[0] == user):
                		print "<p>" + line + "</p>"
        	if(i>19):
            		break
    print   "</body>"
    print "</html>"



