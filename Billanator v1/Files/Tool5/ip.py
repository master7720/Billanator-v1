import os, re, sys, time, json, socket, random
try:
    import requests
except:
    print '*==========*\npip2 install requests\n*==========*'

from urlparse import urlparse
from colorama import Fore, init
from multiprocessing.dummy import Pool as ThreadPool
init(autoreset=True)
white = Fore.LIGHTWHITE_EX
red = Fore.LIGHTRED_EX
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
try:
    os.system('title xRev-IP - @david_3illa')
except:
    pass

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


open('_Reversed.txt', 'a+')
open('ip-reverse.txt', 'a+')
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
c = {'_ga': 'GA1.2.584670167.1608507462', 
   '_gid': 'GA1.2.1162007034.1608507462', 
   '_securitytrails_app': 'QTEyOEdDTQ.qEa1Ib1Q-PQOwueIAkq82G7b5rRGLG4cxBXDMyai6ThYctnNbbUYLGlNXE4.w7yO3vJ36gNW_z6x.IQc0lsQHTKpObeukpk4mmvNUw2uyTKpq8vo-RC1uieeb8i_LrM_eVd5HbOKip0315GTm21a0i_Dh03VF1pohKI2RUGa9lf7i66nsKIdjZ0E7VuDRUXv7oGLcMOsdskM9_OlwjkfUlUHFhF50pCNcgO3iUdwOc6fItc8NaNsUm9Yb8-LnJDJdGl1_7pY6pYd8kIkrZaNIqFRzrHFHJjSzyq3euLMrDTEs5sfa6q2OK2ocu0E9BPF01wqI.ph6hVxWG8AoE8YbOM5kFAQ', 
   '_vwo_uuid_v2': 'DA7D2514D4F55765ADD7630E0AC4BC0BA|290abb2ce3b7361678c3a2e4d88e21f1', 
   'DFTT_END_USER_PREV_BOOTSTRAPPED': 'true', 
   'driftt_aid': 'e361412c-e1fa-46c1-be7c-d17945c6be0e', 
   'driftt_sid': '76ae5193-6ddc-4cd8-ab8f-81f419153dcd', 
   'mp_679f34927f7b652f13bda4e479a7241d_mixpanel': '%7B%22distinct_id%22%3A%20%22176826a0406500-0471a33fb9abb2-c791039-100200-176826a0407781%22%2C%22%24device_id%22%3A%20%22176826a0406500-0471a33fb9abb2-c791039-100200-176826a0407781%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecuritytrails.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22securitytrails.com%22%2C%22app%22%3A%20%22Console%22%7D'}
Ban = ' ' + green + '''
  ____  _ _ _                   _             
 |  _ \(_) | | DavidBilla      | |            
 | |_) |_| | | __ _ _ __   __ _| |_ ___  _ __ 
 |  _ <| | | |/ _` | '_ \ / _` | __/ _ \| '__| 
 | |_) | | | | (_| | | | | (_| | || (_) | |   
 |____/|_|_|_|\__,_|_| |_|\__,_|\__\___/|_|   
                                              
 The Most Advanced IP-Reverse tool 
    \n'''

def ban():
    try:
        print Ban
    except:
        print 'Check your signal!'
        exit()


def rev(url):
    global badrev
    global headers
    global total
    global totalrev
    try:
        url = url.strip()
        url = url.replace('\n', '').replace('\r', '')
        if '://' in url:
            url = urlparse(url)
            url = url.netloc
        else:
            url = url
        ips = socket.gethostbyname(url)
        if '.' in ips or ':' in ips:
            if ips not in open('ip-reverse.txt', 'r').read():
                open('ip-reverse.txt', 'a').write(ips + '\n')
        for i in range(1, 101):
            i = str(i)
            rev = requests.post('https://securitytrails.com/app/api/v1/list_new/ip/' + ips + '?page=' + i, headers=headers, cookies=c, timeout=15)
            rev = rev.text
            if '"hostname":' in rev:
                domain = True
                grab = re.findall('"hostname":"(.*?)"', rev)
                for k in grab:
                    k = k.replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '')
                    if k.replace('www.', '') not in open('_Reversed.txt', 'r').read():
                        total += 1
                        totalrev += 1
                        open('_Reversed.txt', 'a').write('https://' + k + '/\n')

            else:
                break

        domain = True
    except:
        domain = False

    if domain:
        print '' + white + '[>>] ' + str(url) + ' ' + cyan + '[ Reversed ] >> ' + green + '[' + str(total) + ' Sites]' + green + '' + white + ''
        total = 0
        os.system('title xRev-IP - Domain: [' + str(xyz) + ']  Grabbed: [' + str(totalrev) + ']')
    elif domain:
        print '' + white + '[>>] ' + str(url) + ' ' + cyan + '[ Reversed ] >> ' + green + '[' + str(total) + ' Sites]' + green + '' + white + ''
        total = 0
        os.system('title xRev-IP - Domain: [' + str(xyz) + ']  Grabbed: [' + str(totalrev) + ']')
    else:
        kaka = 0
        print '' + white + '[>>] ' + str(url) + ' ' + red + '[ Failed ] >> [' + str(total) + ']' + white + ''
        badrev += 1
        os.system('title xRev-IP - Domain: [' + str(xyz) + ']  Grabbed: [' + str(totalrev) + ']')


if __name__ == '__main__':
    try:
        clear()
        ban()
        try:
            targety = raw_input('' + white + '~# list : ')
        except:
            print 'Invalid'

        bayy = raw_input('' + red + '~# thread : ')
        try:
            pool = ThreadPool(int(bayy))
        except:
            pass

        xyz = 0
        target = open(targety, 'r').readlines()
        for ex in target:
            xyz += 1

        print '[ ' + red + 'Reversing ' + white + ']'
        total = 0
        badrev = 0
        totalrev = 0
        pool.map(rev, target)
        pool.close()
        pool.join()
    except IOError as io:
        print ('Error : {}').format(io)