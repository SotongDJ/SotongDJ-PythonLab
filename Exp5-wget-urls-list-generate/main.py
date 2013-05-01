#!/usr/bin/env python
dsln="-------------------------"
print dsln
print "How many DIGITS do you want?"
digit=raw_input()
print dsln
print "What is the first number?"
first=raw_input()
print dsln
print "What is the last number?"
last=raw_input()
print dsln
print "What is the string before the numbers?"
b4=raw_input()
print dsln
print "What is the string after the numbers?"
after=raw_input()
print dsln
print "Generating... (and writing...)"
result=open("urls.txt",'w')
for a in range(int(first),int(last)+1):
    if len(str(a)) < int(digit):
        b=str(a)
        for n in range(0,int(digit)-len(str(a))):
            b="0"+b
    elif len(str(a)) == int(digit):
        b=str(a)
    else:
        print "Error: the digits of proceed number to high"
    result.write(b4+b+after+'\n')
result.close()
print dsln
