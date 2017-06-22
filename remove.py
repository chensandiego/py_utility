import os
import time
emptyDirs = []
path = "\\\\192.168.90.2\\123\\old"

def deleteFiles(dirList, dirPath,age):

	#will loop through a directory and try to determine if a file is more than 60 days old. if it does, the program will delete it
     for file in dirList:

            now=time.time()
            filepath = os.path.join(dirPath, file)
            modified = os.stat(filepath).st_mtime
            if modified < now - age:
                   if os.path.isfile(filepath):
                         os.remove(filepath)

def removeDirectory(dirEntry):
    print ("Deleting files in " + dirEntry[0])

	#run the deletefiles function
	deleteFiles(dirEntry[2], dirEntry[0],(60 * 86400))


tree = os.walk(path)



for directory in tree:
    removeDirectory(directory,)
