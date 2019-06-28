"""
A simple python script to rename files.
Saket Roy, June 14th 2019.
"""

import os, sys

"""
path must contain the path to the directory with the required files. 
Note: '\' must be escaped as "\\" 
"""
path = "..."

"listdir returns a list of all files contained in the directory"
files = os.listdir(path)

"Rename file by changing old file pathname with an updated one"
for filename in files:
    origPath = path + "\\" + filename
    
    "Store in filename the name you want to rename the file to"
    "Note: Remember to add the necessary extension"
    filename = '...'

    newPath = path + "\\" + filename
    os.rename(origPath, newPath)
     
