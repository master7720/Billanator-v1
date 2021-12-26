import re , urllib.request, urllib.error, urllib.parse  , sys , os, requests
from platform import system
from time import sleep
from threading import Thread
import time
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[1;32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[38m' 
C  = '\033[36m'
GR = '\033[37m' 
def slowprint(s):
    for c in s + '\
':
        sys.stdout.write(c)
        sys.stdout.flush() 
        time.sleep(8./90)
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

banner =  '''
  ____  _ _ _                   _             
 | __ )(_) | | __ _ _ __   __ _| |_ ___  _ __ 
 |  _ \| | | |/ _` | '_ \ / _` | __/ _ \| '__|
 | |_) | | | | (_| | | | | (_| | || (_) | |   
 |____/|_|_|_|\__,_|_| |_|\__,_|\__\___/|_|   
                                              
A Private Tool To Remove Duplicates

https://t.me/tutorials_zone
'''
print(banner)
print("Created By DavidBilla\
")
a = input('[>>] Enter Name list >> ')
c = open(a , 'r').readlines()
c_set = set(c)
aa = input('[<<] Enter Name Output list >> ')
dz = open(aa , 'w')
for line in c_set:
    dz.write(line)
