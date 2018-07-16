#!/bin/python

number=input("Enter number")
fact=1
i=number
while i>=1:
    fact=fact*i
    i=i-1

print "factorial of",number , "is" ,  fact

