#!/mnt/us/python/bin/python2.6
#coding=UTF8
import os
import sys
## defination -- start-----------------------------
dsln="-------------------------"
key1=""
key2=""
digit=""
numsum=""
global tmps,tmpl,blank,argv
tmps=""
tmpl=[]
blank=""
argv=""
#def clean():
#    os.system("rm /tmp/pytmp")
## defination -- end-------------------------------
##
# clean()
##
rsfl=open("combination.txt","w")
rsft=open("resut.txt","w")
##
os.system("clear")
print "Welcome!"
print dsln
print "First, tell me the digit of the numbers which you want."
print dsln
digit=raw_input()
# key1=raw_input()
# if key1 == blank:
#     print "Input Format Error:Please re-open program."
# elif str(int(key1))==key1:
#     numsum=key1
# else:
#     print "Input Format Error:Please re-open program."
##
# clean()
##
a=dsln+"\n"+"The digit of numbers: "+str(digit)+"\n"+dsln
print a
rsfl.write(a+"\n")
rsft.write(a+"\n")
print "Second, what is the sum of the numbers which you want?"
print dsln
numsum=raw_input()
# key2=raw_input()
# if key2 == blank:
#     print "Input Format Error:Please re-open program."
# elif str(int(key2))==key2:
#     numsum=key2
# else:
#     print "Input Format Error:Please re-open program."
##
# clean()
##
b="The sum of numbers: "+numsum+"\n"+dsln
print b
rsfl.write(b+"\n")
rsft.write(b+"\n")
##
print "What number you was select?"
selnumst=raw_input()
selnum=int(selnumst)
print dsln
c="The number that you selected: "+selnumst+"\n"+dsln
print c
rsft.write(c+"\n")
##
numrange=1
stat=0
for a in range(0,int(digit)):
    numrange=numrange*10
numofprev=0
numofgen=1
##
if digit <=5:
    numofdec=100
    noddif=100
elif digit >6:
    numofdec=10000
    noddif=10000
elif digit>5:
    numofdec=1000
    noddif=1000
##
for num1 in range(0,numrange):
    num2=0
    for string in str(num1):
        num2=num2+int(string)
    if num2==int(numsum):
        rsfl.write(str(num1)+"\n")
        if numofprev<10:
            if num1 >= selnum:
                stat=1
                print "The next "+str(numofprev+1)+"th combination is:"
                rsft.write("The "+str(numofprev+1)+"th combination is:\n"+str(num1)+"\n")
                print str(num1)
                numofprev=numofprev+1
        numofgen=numofgen+1
        if numofgen == numofdec:
            print dsln
            print "I just generate "+str(numofgen)+" combination."
            print dsln
            numofdec=numofdec+noddif
rsft.write(dsln+"\nTotal generate "+numofgen+" combination\n"+dsln)
rsfl.close()
rsft.close()
##
#stat=0
#print "The next combination is:"
#for line in open("result.txt").read().splitlines():
#    if int(line) == selnum:
#        stat=1
#    if stat==1:
#        print line
