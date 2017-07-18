#bashCommand = "convert -density 300 3.pdf -quality 90 3-jpg.jpg"
import subprocess
import os
from os.path import basename

directory_in_str="/home/chen/Downloads/AN/"


for subdir, dirs, files in os.walk(directory_in_str):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".pdf"):
            base=os.path.basename(filepath)
            file_to_convert=os.path.splitext(base)[0]
            bashCommand = "convert -density 300 " +file_to_convert+".pdf"+" -quality 90 "+file_to_convert+"-jpg.jpg"
            os.system(bashCommand)
            print(bashCommand)
            print (filepath)
            print (file_to_convert)
