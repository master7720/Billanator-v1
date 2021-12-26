import re, requests
from colorama import Fore
banner = '''

 ______  _________ _        _        _______  _        _______ _________ _______  _______ 
(  ___ \\ \\__   __/( \\      ( \\      (  ___  )( (    /|(  ___  )\\__   __/(  ___  )(  ____ )
| (   ) )   ) (   | (      | (      | (   ) ||  \\  ( || (   ) |   ) (   | (   ) || (    )|
| (__/ /    | |   | |      | |      | (___) ||   \\ | || (___) |   | |   | |   | || (____)|
|  __ (     | |   | |      | |      |  ___  || (\\ \\) ||  ___  |   | |   | |   | ||     __)
| (  \\ \\    | |   | |      | |      | (   ) || | \\   || (   ) |   | |   | |   | || (\\ (   
| )___) )___) (___| (____/\\| (____/\\| )   ( || )  \\  || )   ( |   | |   | (___) || ) \\ \\__
|/ \\___/ \\_______/(_______/(_______/|/     \\||/    )_)|/     \\|   )_(   (_______)|/   \\__/
                                                                                          

Advanced site Grabber
 '''
print(banner)
David = input('root@DavidBilla:~# Domains By Day : ')
Billa = input('root@DavidBilla:~# Domains by Month : ')
for i in range(15):
    i = int(i) + 1
    print('Site: ' + str(i))
    x = requests.get('https://www.cubdomain.com/domains-registered-by-date/2021-' + str(Billa) + '-' + str(David) + '/' + str(i))
    r = re.findall('">(.*?)</a>\n</div>', x.text)
    sv = open('grabbed.txt', 'a')
    for z in r:
        if '/' in z or '=' in z or 'Download Extension' in z:
            pass
        else:
            print(z)
            sv.write(z + '\\n')

    print('DomainResults: ' + str(len(r)))
