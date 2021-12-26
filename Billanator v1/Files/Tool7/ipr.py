def scan(site):
    ur = site.rstrip()
    ch = site.split('\n')[0].split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.'
    i = 0
    while i <= 255:
        i += 1
        c = 0
        while c <= 255:
            c += 1
            print('Ranging ==>' + str(taz) + str(c) + '.' + str(i))
            open('Result/range.txt', 'a').write(str(taz) + str(c) + '.' + str(i) + '\n')


banner = '''
  ____  _ _ _                   _             
 |  _ \(_) | | DavidBilla      | |            
 | |_) |_| | | __ _ _ __   __ _| |_ ___  _ __ 
 |  _ <| | | |/ _` | '_ \ / _` | __/ _ \| '__|
 | |_) | | | | (_| | | | | (_| | || (_) | |   
 |____/|_|_|_|\__,_|_| |_|\__,_|\__\___/|_|   
                                              
'''

print(banner)
print('IP Range Grabber By DavidBilla')
nam = input('List Ips : ')
with open(nam) as (f):
    for site in f:
        scan(site)
