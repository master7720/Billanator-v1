import socket, requests, re, sys, threading
from queue import Queue
from colorama import Fore, init
from itertools import cycle
from multiprocessing.dummy import Pool as ThreadPool
white = Fore.LIGHTWHITE_EX
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.CYAN

def taz(ip):
    try:
        ip = ip.replace('\n', '').replace('\r', '')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, 80))
        if str(result) != '0':
            print(red + '[xx] Bad Ip >>> ' + ip + white)
            open('Result/Badip.txt', 'a').write(ip + '\\n')
        if str(result) == '0':
            print(cyan + '[>>] Good Ip >>> ' + ip + white)
            open('Result/Goodip.txt', 'a').write(ip + '\\n')
    except:
        pass


banner =  '''
                   
  ____  _ _ _                   _             
 | __ )(_) | | __ _ _ __   __ _| |_ ___  _ __ 
 |  _ \\| | | |/ _` | '_ \\ / _` | __/ _ \\| '__|
 | |_) | | | | (_| | | | | (_| | || (_) | |   
 |____/|_|_|_|\\__,_|_| |_|\\__,_|\\__\\___/|_|   
                                              
A Private Tool To Check GoodIPS


'''

print(banner)
David = open(input(''  ' list :  ' ''), 'r').readlines()
Davidd = input(''  ' thread : '  '')
pool = ThreadPool(int(Davidd))
pool.map(taz, David)
pool.close()
pool.join()
if __name__ == '__main__':
    print('Done !! Check /Result/Goodip.txt !!')
