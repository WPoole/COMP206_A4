#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi
#userPath="/home/2016/eayded/public_html/users.txt"
userPath="users.txt"
userArray=[]
userNameIndex=0
loginUser = ""
form=""
fullNameIndex=2
top="<html><body style='background-color:lightgrey'><h2 style='color:Navy'>Make new friendgineers!</h2>"
goback=''
closing= "</body></html>"
#function that tries to open the user file and populate the user array
def getCurrentUser():
	global loginUser
	form=cgi.FieldStorage()
	loginUser=form.getvalue("username")
def buildForm():
	global form
	global loginUser
	global goback
	form='<form action="newfriends.py" method="get">'
	for user in userArray:
		currentUser=user[userNameIndex]
		currentName=user[fullNameIndex]
		if currentUser!=loginUser:
			form=form+'<input type="checkbox" name="'+currentUser+'" value="selected">'+currentName.replace("+"," ")+" : "+currentUser+'<br>'
	form=form+'<input type="hidden" name="username" value="'+loginUser+'">'	
	form=form+'<input type="submit" value="Add a Friend!"></form>'
	goback='<form action="dashboard.py" method="get"><input type="hidden" name="username" value="'+loginUser+'"><input type="submit" name="return" value="Return to Dashboard"></input><br></form>'
#this function reads all of the user and place them in an array, doenst exclude the current user
def populateUsersArray():
	try:
		UserFile=open(userPath,"r")
		line=UserFile.readline()
		while True:
			newUser=[]
			for index in range(0,4):
				line=line.replace("\n","")
				newUser.append(line)
				line=UserFile.readline()
			
			userArray.append(newUser)
			if not line: break
		buildForm()
	except IOError:
		print "error"
	UserFile.close()
#function that 
def renderHTML():
	global form
	global goback
	print "Content-Type: text/html;charset=utf-8"
	print
	print top
	print form
	print goback
	print closing
getCurrentUser()
populateUsersArray()
buildForm()
renderHTML()
