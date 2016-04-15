import cgi

form = cgi.FieldStorage()
friend = form.getvalue('username')+"\n"
#friend = "Flo\n"

userFile = open("users.txt","r")
username = userFile.readline()
print "Content-Type: text/plain;charset=utf-8"
print ""

print "%s" % friend
