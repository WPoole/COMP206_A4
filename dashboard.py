#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi

form = cgi.FieldStorage()

user = form.getvalue('username')

print "Content-Type: text/plain;charset=utf-8"
print "Content-type:text/html\r\n\r\n"
print ""
print "<html>"
print "<head>"
print "<title>Dashboard</title>"
print "</head>"
print "<body style='background-color:lightgrey;'>"
print "<h1 style='color:Navy;'>Welcome to your Personal Dashboard %s!</h1>" % (user)
print "<h3>Menu: </h3>"
print "<form action=\"/~frober6/welcome.html\" method=\"get\">"
print "<button>Logout</button>"
print "<input type=\"hidden\" name=\"username\" value=\"%s\">" % (user)
print "</form>"
print "<form action=\"makefriends.py\" method=\"get\">"
print "<button>Make a Friend</button>"
print "<input type=\"hidden\" name=\"username\" value=\"%s\">" % (user)
print "</form>"
print "<form action=\"seefriends.cgi\" method=\"get\">"
print "<button>See a Friend</button>"
print "<input type=\"hidden\" name=\"username\" value=\"%s\">" % (user)
print "</form>"
print ""
print "<br>"
print "<br>"
print "<br>"
print ""
print "<form name=\"form\" action=\"status.py\" method=\"get\">"
print "Status Update: <input type=\"text\" name=\"status\">"
print "<input type=\"submit\" value=\"Update Status\" />"
print "<input type=\"hidden\" name=\"username\" value=\"%s\">" % (user)
print "</form>"


print     "<br> <h2 style='color:Navy;'><u>Status Updates from You and Your Friends</u></h2>"
usernameAndFriends = None

with open("friends.txt") as f:
    for line in f:
        if(line.split(' ', 1)[0] == user):
            usernameAndFriends = line
            break
if(usernameAndFriends != None):
    usernameList = usernameAndFriends.split()
    # print(usernameList)

    i=0
    for line in reversed(list(open("status.txt"))):
            i+=1
            for usern in usernameList:
                    if(line.split(' ', 1)[0] == usern):
                            print "<p>" + line + "</p>"
            if(i>19):
                    break




print "</body>"
print "</html>"
