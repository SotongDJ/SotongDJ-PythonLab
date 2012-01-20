import os
## defination -- start-----------------------------
dsln="-------------------------"
key1=""
line1=""
loc=""
def clean():
	tmpl=[]
	blank=""
clean()
## defination -- end-------------------------------
##
## locate directory -- start-----------------------
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
## locate directory -- end-------------------------
##
## list file -- start-----------------------------------
os.system("ls "+loc+">/tmp/pytmp")

## list file -- end------------------------------------
