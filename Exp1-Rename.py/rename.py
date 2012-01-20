import os
## defination start--------------------------------
dsln="-------------------------"
key1=""
blank=""
line1=""
loc=""
tmp=[]
## defination end----------------------------------
print "Welcome!"
print dsln
print "First, tell me the folder which you want to clean up, current?"
print "If the answer is \"Yes\", press ENTER key."
print "If not, please key-in the location:"
print dsln
key1=raw_input()
if key1 == blank:
	os.system("pwd>/tmp/pytmp")
	tmp=open("/tmp/pytmp").read().splitlines()
	if len(tmp) == 1:
		for line1 in tmp:
			loc=line1
	else:
		print "Input Format Error:Please re-open program."
else:
	loc=key1
#os.system("echo "+loc) --debugUsage

