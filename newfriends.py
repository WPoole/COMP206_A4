#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi
import cgitb
friendArray=[]
existing=[]
loginUser=""
toAdd=""
userPath='friends.txt'
makeFriendLink=''
dashBoard=""

def loadGetForm():
	global loginUser
	global frienArray
	global dashboard
	global makeFriendLink
	form=cgi.FieldStorage()
	for key in form.keys():
		user=str(key)
		if user=="username":
			loginUser=form.getvalue("username")
		else:
			user=user.replace(" ","")
			friendArray.append(user)
	dashBoard='<form action="dashboard.py"><input type="hidden" name="username" value="'+loginUser+'"> <input type="submit"value="Return to Dashboard"></form>'
	makeFriendLink='<form action="makefriends.py"><input type="hidden" name="username" value="'+loginUser+'"><input type="submit"value="Return to Make a Friend page"></form>'
#function that compares existing and toadd to remove duplicates
def friendToAdd():
	global toAdd
	global existing
	global friendArray
	global loginUser
	for newfriends in friendArray:
		shouldAdd=True
		for friends in existing:
			if friends==newfriends:
				shouldAdd=False
				break
		if shouldAdd:
			existing.append(newfriends)
	toAdd=loginUser+" "
	for friends in existing:
		friends=friends.replace(' ','')
		if friends!="":
			toAdd=toAdd+friends+" "
	toAdd=toAdd+"\n"
def updateFriends():
	global loginUser
	global toAdd
	global existing
	global userPath
	try:
		userFile=open(userPath, "r")
		friendFile=userFile.readlines()
	except IOError:
		print "error in reading"
	userFile.close()
	try:
                userFile=open(userPath, "r+")
		i=0
		userIndex=0
		for line in friendFile:
			line=line.replace("\n","")
			token=line.split(" ")
			if token[0]==loginUser:
				userIndex=i
				for tok in token:
					tok=tok.replace(" ","")
				existing=token[1:]
				friendToAdd()
			i+=1
		i=0	
		for line in friendFile:
			if i==userIndex:
				userFile.write(toAdd)
			else:
				userFile.write(line)
          		i+=1
        except IOError:
                print "error in writing"

	userFile.close()
def renderHtml():
	global loginUser
	global friendArray
	global makeFriendLink
	global dashBoard
	global toAdd
	print "Content-Type: text/html;charset=utf-8"	
	print
	print "<htm><body style='background-color:lightgrey'><h2 style='color:Navy'>You just made new friendgineer friends!</h2>"
	print makeFriendLink
	print dashBoard
	print "</body></html>"
loadGetForm()
updateFriends()
renderHtml()

