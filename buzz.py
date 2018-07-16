#!/bin/python

for i in range(1,100):
    if i%6==0 and i%4==0:
        print "linkedin"
    elif i%6==0:
        print "Linked"
    elif i%4==0:
        print "In"
    else:
        print i

