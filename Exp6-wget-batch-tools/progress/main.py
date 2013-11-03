import os
def status():
    print "----RESULT-----------"
    os.system("ls -1>progress/file.tmp")
    for wgetlog in open("progress/file.tmp").read().splitlines():
        if "wget-log" in wgetlog:
            percentage="0%"
            for line in open(wgetlog).read().splitlines():
                if "K ." in line or "100%" in line or "K =" in line:
                    if "100%" not in line:
                        #print "mark0:"+percentage
                        tpo=int(percentage.replace("%",""))
                        for sect in line.split(" "):
                        #    print "rub:"+sect
                            if "%" in sect:
                                a=sect
                        #print "a:"+a
                        #print "mark1:"+percentage
                        tpn=int(a.replace("%",''))
                        if tpn > tpo:
                            percentage=a
                        #    print "mark2:"+percentage
                        #print "mark3:"+percentage
                    elif "100%" in line:
                        percentage="Finished"
            print wgetlog+":"+percentage
    print "---------------------"
command="i"

while command!="n":
    command=raw_input("Which you want?\n\"w\" for start a new wget process\n\"c\" for check the status and repeat this sctipt\n\"n\" for the end\nYour selection:\n")
    if command=="w":
        os.system("wget -bc \""+raw_input("Copy and paste your target url:\n")+"\"")
    elif command=="c":
        status()
