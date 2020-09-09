import os
import sys
import time

def logo():
	print """

	 _______                                             
	 \      \   _____ _____  ______ ______   ___________ 
	 /   |   \ /     \\__  \ \____ \\____ \_/ __ \_  __ \
	/    |    \  Y Y  \/ __ \|  |_> >  |_> >  ___/|  | \/
	\____|__  /__|_|  (____  /   __/|   __/ \___  >__|   
	        \/      \/     \/|__|   |__|        \/       
"""

def cls():
	os.system("clear")

print "Installing Requirements...."
time.sleep(0.3)
os.system("sudo apt-get install nmap")
os.system("pkg install nmap")

cls()
logo()
print
print "[1] Scan a Website"
print "[2] Scan an Ip Address"
print "[3] Advance Options"
print 
nmaper=raw_input("Enter Your Choice :")
#Frontend Done

if nmaper == '1' or nmaper == '01':
	Website=raw_input("Enter Target Website : ")
	os.system("nmap -v -A %s" % (Website))
	print
	print "Scanning Completed"

elif nmaper == '2' or nmaper == '02':
	ip=raw_input("Enter Target Ip :")
	os.system("nmap -v -sn %s" % (ip))
	print
	print "Scanning Completed"
elif nmaper == '3' or '03':
	os.system("nmap")
else:
	print "Wrong Input !"

#FINISHED
