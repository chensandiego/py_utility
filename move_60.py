import os
import time
import subprocess
import shutil
emptyDirs = []
path = "\\\\192.168.30.118\\abc\\aa\\"
destpath="\\\\192.168.30.118\\123\\old\\"

def moveDirectory(dirNames):
	for dirName in dirNames[1]:
		currentDir=path+dirName
		destDir=destpath+dirName
		now=time.time()
		age=60*86400
		for file in os.listdir(currentDir):

			src_file=os.path.join(currentDir,file)

			modified = os.stat(src_file).st_mtime


			##check if a file is more than 30 days
			##if it is, i will move it to the archive folder

			if modified < now - age:
				dest_file=os.path.join(destDir,file)
				shutil.move(src_file,dest_file)
#			print "move from" + src_file
				print ("To "+dest_file +"\n")


def checkDirectory(dirNames):
	for dirName in dirNames[1]:
		newdir=destpath+dirName
		if not os.path.exists(newdir):
			os.makedirs(newdir)

tree = os.walk(path)



for directory in tree:

	#check if users directories are exist
	#if user directories are not exist, it will create a user directory
    checkDirectory(directory,)

	#start to move files
    moveDirectory(directory,)
