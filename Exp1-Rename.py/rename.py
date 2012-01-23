import os
import sys
## defination -- start-----------------------------
dsln="-------------------------"
key1=""
loc=""
filelist1=[]
filelist2=[]
chlist=[]
global tmps,tmpl,blank,line1,line2,argv
tmps=""
tmpl=[]
blank=""
line1=""
line2=""
argv=""
def clean():
	tmps=""
	tmpl=[]
	blank=""
	line1=""
	line2=""
	os.system("rm /tmp/pytmp")
## defination -- end-------------------------------
##
clean()
## locate directory -- start-----------------------
os.system("clear")
print "Welcome!"
print dsln
print "First, tell me the folder which you want to clean up, current?"
print "If the answer is \"Yes\", press ENTER key."
print "If not, please key-in the location(absolute address): "
print dsln
key1=raw_input()
if key1 == blank:
	os.system("pwd>/tmp/pytmp")
	tmpl=open("/tmp/pytmp").read().splitlines()
	if len(tmpl) == 1:
		for line1 in tmpl:
			loc=line1
	else:
		print "Input Format Error:Please re-open program."
else:
	loc=key1
print "Directory: "+loc
## locate directory -- end-------------------------
##
clean()
## list file -- start-----------------------------------
print "Content files:"
os.system("ls \""+loc+"\"")
os.system("ls -1 \""+loc+"\">/tmp/pytmp")
filelist1=open("/tmp/pytmp").read().splitlines()
## list file -- end------------------------------------
##
clean()
## Identity Previous RD -- start-----------------
status=os.system("cp chlist /tmp/pytmp2")
## Identity Previous RD -- end------------------
##
clean()
## Key-in RD -- start-------------------------------
## des:key-in replacement dictionary
print dsln
print "Now, You can key-in the words you want to replace"
print "into gedit. Please follow the format."
print "  "
print "Notice:Be carefull don't use special symbol like "
print "\"?\", \"=\", \"*\" and \"##\", to prevent error."
print dsln
title="## Example:\nchange_from=change_to ##"
if status == 0:
	os.system("mv /tmp/pytmp2 /tmp/pytmp")
else:
	file=open("/tmp/pytmp",'w')
	file.write(title)
	file.close()
os.system("gedit /tmp/pytmp")
raw_input("If you finish key-in, press ENTER.")
chlist=open("/tmp/pytmp").read().splitlines()
os.system("cp /tmp/pytmp \""+loc+"/chlist\"")
## Key-in RD -- end--------------------------------
## 
clean()
## generate chlist -- start -----------------------
file1=open(loc+"/rename.sh",'w')
file2=open(loc+"/before.list",'w')
file3=open(loc+"/after.list",'w')
file1.write("#/bin/sh\n")
file2.write("Before rename:\n")
file3.write("After rename:\n")
for line1 in filelist1:
	tmps="\""+loc+"/"+line1+"\""
	for line2 in chlist:
		if not "##" in line2:
			tmpl=line2.split("=")
			line1=line1.replace(tmpl[0],tmpl[1])
	line1="\""+loc+"/"+line1+"\""
	file1.write("mv "+tmps+" "+line1+"\n")
	file2.write(tmps+"\n")
	file3.write(line1+"\n")
file1.close()
file2.close()
file3.close()
