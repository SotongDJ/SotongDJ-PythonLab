import os
file=open("target").read()
print file
print "\""+file+"\""
print "\"\\\""
status=os.system("ls -1>pytemp")
file=open("pytemp").read()
file=file.replace('!1','\"')
file=file.replace('!2','\\\"')
print file
