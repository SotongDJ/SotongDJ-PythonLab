import os
## defination -- start-----------------------------
dsln="-------------------------"
key1=""
loc=""
filelist=[]
global tmps,tmpl,blank,line
tmps=""
tmpl=[]
blank=""
line=""
def clean():
	tmps=""
	tmpl=[]
	blank=""
	line=""
## defination -- end-------------------------------
##
clean()
## locate directory -- start-----------------------
os.system("clear")
print "Welcome!"
print dsln
print "First, tell me the folder which you want to clean up, current?"
print "If the answer is \"Yes\", press ENTER key."
print "If not, please key-in the location:"
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
os.system("ls "+loc)
os.system("ls -1 "+loc+">/tmp/pytmp")
filelist=open("/tmp/pytmp").read().splitlines()
## list file -- end------------------------------------
##
clean()
## IRD -- start---------------------------------------
## des:input replacement dictionary
print dsln
print "Now, You can"
print dsln
## IRD -- end----------------------------------------
