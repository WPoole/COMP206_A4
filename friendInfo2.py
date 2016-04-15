#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi

form = cgi.FieldStorage()
friend = form.getvalue('username')
# friend = "a" + "\n"
currentUser=form.getvalue('current')
userFile = open("users.txt","r")
username = userFile.readline()
username = username.replace('\n', "")
username = username.replace(" ", "")
friend = friend.replace(" ", "")
while 1:
        if not username:
            break

        if username==friend:
            passW = userFile.readline()
            passW = passW.replace('\n','')
            fullName = userFile.readline()
            fullName = fullName.replace('\n','')
            jobDesc = userFile.readline()
            jobDesc = jobDesc.replace('\n','')
            print "Content-Type: text/plain;charset=utf-8"
            print "Content-type:text/html\r\n\r\n"
            print ""
            print "<html>"
            print "<body>"
	    print "<h1 style='color:Navy;'>Profile of your friendgineer %s</h1>" % (username)
            print "<p>Friends : %s</p>" % (friend)
            print "<p>Name : %s*</p>" % (fullName)
            print "<p>Job description: %s</p>" % (jobDesc)
            break
        else:
                username = userFile.readline()
                username = username.replace('\n', "")
                username = username.replace(" ", "")

print '<form action="dashboard.py" method="get"><input type="hidden" name="username" value="'+currentUser+'"><input type="submit" name="return" value="Return to Dashboard"></input><br></form>'
print "</body>"
print "</html>"

