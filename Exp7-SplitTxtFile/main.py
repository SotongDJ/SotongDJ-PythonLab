import os
import sys
#setting------------------
dam=4 # digit of your file name
split= "-|-|-" #split digit
#setting------------------
## defination -- start-----------------------------
def turn(num,rang):
    if len(str(num))>rang:
#        print "proa"
        rang=num
    if len(str(num)) == rang:
#        print "prob"
        return str(num)
    else:
        b=str(num)
        zero=rang-len(str(num))
#        print "proc"
        for a in range(0,zero):
            b="0"+b
        return b
lastNum="1"
for c in range(0,dam):
    lastNum=lastNum+"0"
## defination -- end-------------------------------
print "Welcome! I can help you split source.txt into many part"
print "Let's start. First let me know the number of the first part: "
numOf1stFileStr=raw_input()
numOf1stFileInt=int(numOf1stFileStr)
#print turn(numOf1stFileInt,4)
d=numOf1stFileInt
file1=open(turn(d,dam)+".txt",'w')
for line in open("source.txt").read().splitlines():
    if split in line:
        file1.close()
        d=d+1
        file1=open(turn(d,dam)+".txt",'w')
    else:
        file1.write(line+"\n")
file1.close()
    
