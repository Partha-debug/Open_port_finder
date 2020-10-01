#!/bin/python3
#Here we are going to scan an IP through a range of ports to know which one is open.
import sys
import socket
from datetime import datetime
#Define our target
if len(sys.argv) == 2:
#As there should only be two arguments one is the script (aegv[0]) and another is the ip (argv[1]) i.e. there length is 2 
	target = socket.gethostbyname(sys.argv[1])
#Will translate the provided host name in the argument into Ipv4 if not given the Ip here (sys.argv[1]) is same as $1 in bash which is the first argument.
else:
	print("Invalid ammount of arguments" + '\n' + "Usage: ./port scanner.py<ip>")
#Adding a banner
print("-" * 50)
print("Scanning target " + target)
print ("Time started " + str(datetime.now()))
print ("-" * 50)
try:
	for port in range (1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) 
#Here ex is a error indicator if there is resonse from the ip then it will return zero and if there is no responce it will return an error output which indeed is a one.
		if result == 0:
			print("port {} is open".format(port)) 
#It will print the port in the existing format into the {}.
			s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Host name can't be resolved")
	sys.exit()
except socket.error:	
	print("Couldn't connect to server.")
	sys.exit()

