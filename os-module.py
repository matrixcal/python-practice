#!/bin/python
import os
#print os.getcwd()

def list_files(x):
    if os.path.isfile(x):
        print x
        return 0
    else:
        list_files(x)

list_files(os.getcwd())

