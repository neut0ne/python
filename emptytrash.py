#!/usr/local/bin/python

import os
import sys

# delete all files and folders in trash box.
# .zshrc alias: rmtrash

os.chdir('/Users/emma/.Trash')
if len(sys.argv) >= 2:
    if sys.argv[1] == '-t' or sys.argv[1] == '-T':
        os.system("tree ./")
    elif sys.argv[1] == '-l' or sys.argv[1] == '-L':
        os.system("ls -al")
print("cleaning up trashbin...")
os.system("rm -rf *")
print("done")
